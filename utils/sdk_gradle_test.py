import os
import subprocess
import sys

# Gradle 和 AGP版本列表，key为Gradle版本，value为AGP版本
GRADLE_VERSION_DICT = {
    "6.7.1": "4.2.2",
    "8.7": "8.5.2",
    "7.3.3": "7.2.2"
}
# 要测试的SDK版本
SDK_DEPENDENCY_VERSION = "2.18.8"
PROJECT_DIR = "/Users/topjoy/StudioProjects/basicsdk/Android/BasicSDK"  # 测试项目路径
APP_MODULE_PATH = os.path.join(PROJECT_DIR, "app")  # app 模块路径
GRADLE_WRAPPER_PROPERTIES = os.path.join(PROJECT_DIR, 'gradle', 'wrapper', 'gradle-wrapper.properties')
# 初始化结果统计字典
test_results = {}


# 修改 Gradle 版本
def modify_gradle_version(gradle_version):
    print(f"Setting Gradle version to {gradle_version}")

    try:
        # 读取 gradle-wrapper.properties 文件内容
        with open(GRADLE_WRAPPER_PROPERTIES, 'r') as file:
            lines = file.readlines()

        # 修改文件中的 distributionUrl 行
        with open(GRADLE_WRAPPER_PROPERTIES, 'w') as file:
            for line in lines:
                if 'distributionUrl=' in line:
                    file.write(
                        f'distributionUrl=https://services.gradle.org/distributions/gradle-{gradle_version}-bin.zip\n')
                else:
                    file.write(line)
            file.write('\n')
    except FileNotFoundError:
        print(f"Error: {GRADLE_WRAPPER_PROPERTIES} not found.")
        sys.exit(1)


def modify_gradle_build_tools_version(gradle_build_tools_version):
    """
    修改项目级别的build.gradle中的agp版本
    :param gradle_build_tools_version:
    :return:
    """
    print(f"Setting Gradle build tools version to {gradle_build_tools_version}")
    build_gradle_path = os.path.join(PROJECT_DIR, 'build.gradle')
    try:
        with open(build_gradle_path, 'r') as build_file:
            lines = build_file.readlines()

        # 在 dependencies 块中添加 SDK 依赖
        with open(build_gradle_path, 'w') as build_file:
            for line in lines:
                # if 'com.android.tools.build:gradle' in line:
                if line.find('com.android.tools.build:gradle') != -1:
                    build_file.write(
                        f'    classpath "com.android.tools.build:gradle:{gradle_build_tools_version}" \n')
                else:
                    build_file.write(line)
            build_file.write('\n')
    except FileNotFoundError:
        print(f"Error: {build_gradle_path} not found.")
        sys.exit(1)


def modify_compile_sdk_version(gradle_version):
    if gradle_version >= "7.0":
        compile_sdk_version = "34"
    else:
        compile_sdk_version = "33"
    print(f"Setting compileSdkVersion to {compile_sdk_version}")
    build_gradle_path = os.path.join(APP_MODULE_PATH, 'build.gradle')

    try:
        with open(build_gradle_path, 'r') as build_file:
            lines = build_file.readlines()
            for line in lines:
                if 'compileSdk' in line:
                    build_file.write(f'    compileSdk {compile_sdk_version}\n')
                else:
                    build_file.write(line)
        build_file.write('\n')
    except FileNotFoundError:
        print(f"Error: {build_gradle_path} not found.")
        sys.exit(1)


# 引入 SDK 依赖到 app 模块的 build.gradle 的 dependencies 块
def add_sdk_dependency(SDK_DEPENDENCY_VERSION):
    print("Adding SDK dependency to the app module")

    build_gradle_path = os.path.join(APP_MODULE_PATH, 'build.gradle')
    try:
        with open(build_gradle_path, 'r') as build_file:
            lines = build_file.readlines()

        # 在 dependencies 块中添加 SDK 依赖
        with open(build_gradle_path, 'w') as build_file:
            for line in lines:
                if 'com.topjoy:zeussdk-android' in line:
                    build_file.write(f'   implementation "com.topjoy:zeussdk-android:{SDK_DEPENDENCY_VERSION}" \n')

                else:
                    build_file.write(line)
            build_file.write('\n')
    except FileNotFoundError:
        print(f"Error: {build_gradle_path} not found.")
        sys.exit(1)


# 执行 app 模块的构建
def build_app_module(gradle_version):
    print(f"Building app module with Gradle {gradle_version}")

    gradle_command = './gradlew assembleDebug'
    java_17_path = '/Applications/Android Studio.app/Contents/jbr/Contents/Home'
    java_11_path = '/Library/Java/JavaVirtualMachines/jdk-11.0.19.jdk/Contents/Home'
    if gradle_version >= "8.0":
        gradle_command = f'JAVA_HOME="{java_17_path}" ./gradlew assembleDebug'
    else:
        gradle_command = f'JAVA_HOME="{java_11_path}" ./gradlew assembleDebug'
    process = subprocess.Popen(gradle_command, shell=True, cwd=PROJECT_DIR)
    process.wait()

    if process.returncode == 0:
        print(f"Build succeeded with Gradle {gradle_version}!")
        test_results[gradle_version] = 'Success'
    else:
        print(f"Build failed with Gradle {gradle_version}!")
        test_results[gradle_version] = 'Failed'


# 输出测试结果
def print_test_results():
    print("\n========== Test Results ==========")
    for version, result in test_results.items():
        print(f"Gradle {version}: {result}")
    print("==================================")


# 主函数：遍历所有 Gradle 版本并进行 app 模块测试
def main():
    add_sdk_dependency(SDK_DEPENDENCY_VERSION)
    for gradle_version, gradle_tool_version in GRADLE_VERSION_DICT.items():
        modify_gradle_version(gradle_version)
        modify_gradle_build_tools_version(gradle_tool_version)
        build_app_module(gradle_version)

    # 打印每个 Gradle 版本的测试结果
    print_test_results()


if __name__ == "__main__":
    main()
