# 📊 Fundamental Company Analyst

> **AI-Powered Financial Analysis using CrewAI**

A comprehensive fundamental analysis tool that leverages AI agents to perform in-depth company research, financial analysis, and investment insights generation.

---

## 🚀 Features

### 🤖 AI-Powered Analysis Team

- **Company Researcher** - Uncovers cutting-edge developments and business intelligence
- **Financial Analyst** - Analyzes financial statements and identifies trends
- **Valuation Analyst** - Performs DCF and comparable company analysis
- **Macro Sector Analyst** - Provides economic and industry context
- **Risk Sentiment Analyst** - Identifies risks and sentiment trends
- **Reporting Analyst** - Compiles comprehensive investment reports

### 🎯 Analysis Capabilities

- 📈 **Financial Metrics** - Revenue, profitability, and growth analysis
- 🔍 **Market Analysis** - Industry position and competitive landscape
- 📊 **Investment Insights** - Risk assessment and recommendations
- 🌍 **Macro Context** - Economic and sector trend analysis
- ⚠️ **Risk Assessment** - ESG, regulatory, and sentiment analysis

---

## 🏗️ Project Structure

```
fundamental_analyst/
├── 📱 app.py                          # Streamlit web application
├── 📋 company_research_task.md         # Company research output
├── 📋 financial_analysis_task.md       # Financial analysis output
├── 📋 macro_sector_task.md            # Macro/sector analysis output
├── 📋 risk_sentiment_task.md          # Risk/sentiment analysis output
├── 📋 valuation_task.md               # Valuation analysis output
├── 📄 report.md                       # Final comprehensive report
├── 🔧 pyproject.toml                  # Project dependencies
├── 🔒 uv.lock                         # Dependency lock file
├── 📁 knowledge/
│   └── 📝 user_preference.txt         # User preferences
├── 📁 src/fundamental_analyst/
│   ├── 🤖 crew.py                     # CrewAI orchestration
│   ├── 🎯 main.py                     # Main execution script
│   ├── 📁 config/
│   │   ├── 👥 agents.yaml             # AI agent configurations
│   │   └── 📋 tasks.yaml              # Task definitions
│   └── 🛠️ tools/
│       ├── 🔧 custom_tool.py          # Custom analysis tools
│       └── 🔍 serper_tool.py          # Web search integration
└── 🧪 tests/                          # Test files
```

---

## ⚡ Quick Start

### 1️⃣ Prerequisites

- Python 3.8+
- Google Gemini API Key
- Serper API Key (for web search)

### 2️⃣ Installation

```bash
# Clone the repository
git clone <repository-url>
cd fundamental_analyst

# Install dependencies
pip install -r requirements.txt
# or if using uv
uv sync
```

### 3️⃣ Configuration

Set up your environment variables:

```bash
export GEMINI_API_KEY="your-gemini-api-key"
export SERPER_API_KEY="your-serper-api-key"
```

### 4️⃣ Run the Application

```bash
# Start the Streamlit app
streamlit run app.py

# Or run directly with Python
python src/fundamental_analyst/main.py
```

---

## 🎯 AI Agents & Tasks

### 👥 Agent Roles

| Agent                         | Role                   | Specialization                            |
| ----------------------------- | ---------------------- | ----------------------------------------- |
| 🔍 **Company Researcher**     | Senior Data Researcher | Latest developments, business model, news |
| 💰 **Financial Analyst**      | Financial Expert       | Statement analysis, ratios, trends        |
| 📊 **Valuation Analyst**      | Valuation Specialist   | DCF, comparable analysis, fair value      |
| 🌍 **Macro Sector Analyst**   | Economic Expert        | Macro trends, industry analysis           |
| ⚠️ **Risk Sentiment Analyst** | Risk Specialist        | ESG risks, sentiment, regulatory issues   |
| 📝 **Reporting Analyst**      | Report Writer          | Comprehensive report generation           |

### 📋 Analysis Tasks

#### 🏢 Company Research

```yaml
Goal: Uncover cutting-edge developments in {company_name}
Output: 10 key insights about business model, history, leadership, products
```

#### 💹 Financial Analysis

```yaml
Goal: Identify financial strengths, weaknesses, and trends
Output: 10 financial insights from statements and ratios analysis
```

#### 💎 Valuation Analysis

```yaml
Goal: Determine intrinsic value using financial modeling
Output: 10 valuation outcomes with DCF and comparable analysis
```

#### 🌐 Macro & Sector Analysis

```yaml
Goal: Provide economic and industry context
Output: 10 macroeconomic factors impacting the company
```

#### ⚡ Risk & Sentiment Analysis

```yaml
Goal: Identify reputational, regulatory, and ESG risks
Output: 10 key risks and sentiment trends
```

#### 📊 Final Reporting

```yaml
Goal: Create detailed investment report
Output: Comprehensive markdown report with all analysis sections
```

---

## 🖥️ Web Interface

### 🎨 Features

- **🔧 API Configuration** - Secure API key management
- **🏢 Company Input** - Easy company selection with suggestions
- **⚡ Real-time Analysis** - Live progress tracking
- **📊 Interactive Reports** - Rich markdown report display
- **💾 Export Options** - Download reports in multiple formats

### 🚀 Usage

1. **Configure APIs** - Enter your Gemini and Serper API keys
2. **Select Company** - Enter the company name for analysis
3. **Start Analysis** - Click "Start Fundamental Analysis"
4. **View Results** - Review the comprehensive report
5. **Download** - Export the analysis for future reference

---

## 🛠️ Technical Stack

- **🤖 AI Framework**: CrewAI for agent orchestration
- **🧠 Language Model**: Google Gemini 2.5 Flash Preview
- **🌐 Web Search**: Serper API
- **🖥️ Frontend**: Streamlit
- **🐍 Language**: Python 3.8+
- **📦 Package Manager**: UV (optional)

---

## 📈 Sample Output

The analysis generates comprehensive reports covering:

- **Executive Summary** with key investment highlights
- **Business Overview** including model and competitive position
- **Financial Performance** with trend analysis and ratios
- **Valuation Analysis** with multiple methodologies
- **Risk Assessment** covering various risk factors
- **Investment Recommendation** with supporting rationale

---

## 🔧 Configuration

### Environment Variables

```bash
GEMINI_API_KEY=your_gemini_api_key
MODEL=gemini/gemini-2.5-flash-preview-05-20
SERPER_API_KEY=your_serper_api_key
```

### Custom Preferences

Edit `knowledge/user_preference.txt` to customize analysis focus and preferences.

---

## 🚨 Important Notes

- **⚠️ Investment Disclaimer**: This tool is for educational and informational purposes only. Not investment advice.
- **🔑 API Keys**: Keep your API keys secure and never commit them to version control
- **📊 Data Accuracy**: Analysis quality depends on available public information
- **⏱️ Processing Time**: Comprehensive analysis may take several minutes

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💡 Support

Having issues? Check out our [troubleshooting guide](TROUBLESHOOTING.md) or open an issue on GitHub.

---

<div align="center">

**🚀 Ready to analyze your next investment?**

[Get Started](#quick-start) • [View Demo](demo-link) • [Report Issues](issues-link)

---

_Built with ❤️ using CrewAI and Streamlit_

</div>
