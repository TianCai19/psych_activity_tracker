# 心理活动记录与反馈系统

## 简介

这是一个基于 LangChain 和 OpenAI 的心理活动记录与反馈系统。用户可以记录每日的心理活动，系统会根据最近的记录提供有针对性和个性化的反馈。

## 功能

- **添加心理活动记录**: 用户可以输入每日的心理活动记录，系统会保存并展示最近的记录。
- **查看心理反馈**: 根据用户的心理活动记录，生成针对性的反馈和建议。
- **管理记录**: 查看所有记录，删除不需要的记录。
- **选择模型**: 在查看反馈时，用户可以选择不同的 OpenAI 模型来生成反馈。
- **历史记录**: 保留最近一周的心理活动记录，方便用户回顾。

## 安装

1. **克隆仓库**:

    ```bash
    git clone https://github.com/你的仓库地址.git
    cd psych_activity_tracker
    ```

2. **创建虚拟环境** (可选):

    ```bash
    python -m venv venv
    source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
    ```

3. **安装依赖**:

    ```bash
    pip install -r requirements.txt
    ```

4. **安装开发和测试依赖**:

    ```bash
    pip install -r requirements-dev.txt
    ```

5. **设置环境变量**:

    您可以选择使用环境变量或 `.env` 文件来配置 OpenAI API 的密钥和 Base URL。

    - **使用环境变量**:

        - 在 Linux/macOS:

            ```bash
            export OPENAI_API_KEY="你的OpenAI_API_KEY"
            export OPENAI_API_BASE_URL="https://your-custom-endpoint.com/v1"  # 可选，默认为 OpenAI 官方 API
            ```

        - 在 Windows:

            ```cmd
            set OPENAI_API_KEY=你的OpenAI_API_KEY
            set OPENAI_API_BASE_URL=https://your-custom-endpoint.com/v1  # 可选，默认为 OpenAI 官方 API
            ```

    - **使用 `.env` 文件**（跨平台）:

        1. 在项目根目录下创建一个 `.env` 文件。
        2. 添加以下内容：

            ```dotenv
            OPENAI_API_KEY=你的OpenAI_API_KEY
            OPENAI_API_BASE_URL=https://your-custom-endpoint.com/v1  # 可选，默认为 OpenAI 官方 API
            ```

        3. 确保 `.env` 文件被正确加载，`config.py` 已包含 `load_dotenv()`。

    **注意**：将 `.env` 文件添加到 `.gitignore` 中，以避免将敏感信息提交到版本控制系统。

## 使用

### 启动应用

```bash
streamlit run main.py
```

### 使用 `uv` 运行测试脚本

您可以使用 `uv` 来运行 `test_langSmith_conversation_v2.py` 脚本，而无需启动 conda 或记住环境名称和切换命令。

```bash
uv run test_langSmith_conversation_v2.py
```
