# ShadowLogic 贡献指南

感谢您对 **ShadowLogic** 的关注和支持！本文档将指导您如何为项目做出贡献。

## 行为准则

我们致力于创建一个开放、包容和尊重的社区。所有参与者都应遵守以下准则：

- **尊重他人**：尊重不同的观点和经验。
- **建设性沟通**：以建设性的方式提出意见和建议。
- **保护隐私**：不分享他人的个人信息。
- **遵守法律**：所有贡献必须遵守适用的法律法规。

## 报告问题

如果您发现了 Bug 或有改进建议，请通过以下步骤报告：

1. 检查 [Issues](https://github.com/ADA-XiaoYao/ShadowLogic/issues) 中是否已有相关报告。
2. 如果没有，请创建一个新的 Issue，并提供以下信息：
   - 问题的清晰描述。
   - 复现步骤。
   - 预期行为和实际行为。
   - 您的环境信息（Python 版本、操作系统等）。

## 提交拉取请求 (Pull Request)

我们欢迎您提交 Pull Request 来改进项目。请按照以下步骤操作：

### 1. Fork 仓库

点击 GitHub 页面右上角的 "Fork" 按钮，将项目复制到您的账户。

### 2. 克隆您的 Fork

```bash
git clone https://github.com/YOUR_USERNAME/ShadowLogic.git
cd ShadowLogic
```

### 3. 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

### 4. 进行更改

在您的分支上进行必要的更改。请遵循以下代码规范：

- **代码风格**：遵循 PEP 8 Python 代码风格指南。
- **注释**：为复杂逻辑添加清晰的注释。
- **文档**：更新相关文档以反映您的更改。
- **测试**：为新功能添加相应的测试。

### 5. 提交更改

```bash
git add .
git commit -m "feat: 添加新功能描述"
```

请使用清晰、简洁的提交信息，遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范。

### 6. 推送到您的 Fork

```bash
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request

在 GitHub 上创建 Pull Request，并提供以下信息：

- 您的更改的清晰描述。
- 相关的 Issue 号（如果有）。
- 测试步骤。

## 代码规范

### Python 代码风格

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范。
- 使用 4 个空格进行缩进。
- 行长度不超过 100 字符。

### 函数和类文档

为所有公共函数和类添加文档字符串：

```python
def analyze_vulnerability(data):
    """
    分析漏洞数据。
    
    Args:
        data (str): 漏洞数据。
        
    Returns:
        str: 分析结果。
    """
    pass
```

## 开发环境设置

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行测试

```bash
python -m pytest
```

## 许可证

通过提交 Pull Request，您同意您的贡献将在 MIT 许可证下发布。

## 联系方式

如有任何问题或建议，请通过以下方式联系我们：

- 在 [Issues](https://github.com/ADA-XiaoYao/ShadowLogic/issues) 中提问。
- 发送电子邮件至项目维护者。

感谢您的贡献！
