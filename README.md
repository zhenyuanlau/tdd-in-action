# 测试驱动开发实战

## Python Web开发

### 命令
```bash
# 启动 Diango 的开发服务器
python3 manage.py runserver

# 运行功能测试
python3 functional_tests.py

# 运行单元测试
python3 manage.py test
```

### 概念

- 用户故事
  > 从用户的角度描述应用应该如何运行。用来组织功能测试。

- 预期失败
  > 意料之中的失败。

- “单元测试/编写代码”循环
  > - 在终端里运行单元测试
  > - 在编辑器中改动最少量的代码
  > - 重复上两步
