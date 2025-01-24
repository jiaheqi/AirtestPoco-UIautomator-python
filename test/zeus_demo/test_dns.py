# import dns.resolver
#
#
# def test_dns_failure():
#     # 设置要查询的域名
#     domain = "zeus.youle.game"  # 替换为您要测试的域名
#
#     # 创建 DNS 解析器
#     resolver = dns.resolver.Resolver()
#
#     try:
#         # 查询域名的 A 记录（IP 地址）
#         answers = resolver.query(domain, "A")
#
#         # 如果查询到结果，输出 IP 地址
#         for answer in answers:
#             print(f"IP 地址：{answer.address}")
#     except dns.resolver.NXDOMAIN:
#         # 捕获 NXDOMAIN 错误，表示域名不存在
#         print(f"域名 {domain} 不存在")
#     except dns.resolver.NoAnswer:
#         # 捕获 NoAnswer 错误，表示无法获取响应
#         print(f"无法获取域名 {domain} 的响应")
#     except dns.resolver.Timeout:
#         # 捕获 Timeout 错误，表示查询超时
#         print(f"查询域名 {domain} 超时")
#     except dns.resolver.NoNameservers:
#         # 捕获 NoNameservers 错误，表示找不到 DNS 服务器
#         print(f"找不到 DNS 服务器")
#     except dns.resolver.NoRootSOA:
#         # 捕获 NoRootSOA 错误，表示无法找到根域的 SOA 记录
#         print(f"无法找到根域的 SOA 记录")
#     except Exception as e:
#         # 捕获其他异常
#         print(f"发生其他错误：{e}")
#
#
# if __name__ == '__main__':
#     # 调用测试函数
#     test_dns_failure()
