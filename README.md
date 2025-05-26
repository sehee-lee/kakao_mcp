# MCP Project using Kakao Developers API

---

## 📌 프로젝트 소개

- **프로젝트 명**: Kakao Search MCP
- **주요 기능**:
  - 다음 카페 게시글 검색
  - 웹문서 검색
  - 블로그 검색
  - 책 검색
  - 이미지/동영상 검색
- **사용한 Kakao API**:
  - [kakao cafe search API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-cafe)
  - [kakao web search API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-doc)
  - [kakao blog search API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-blog)
  - [kakao book search API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-book)
  - [kakao image search API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-image)
  - [kakao video search API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-video)

---

## 🛠 기술 스택

| 분류       | 기술명                       |
|------------|---------------------------|
| Language   | Python                    |
| API        | Kakao Developers REST API |

---

## 🔐 환경 변수 설정 (.env)

```env
KAKAO_APP_KEY=your_kakao_developers_app_key
```

## 🚀 실행 방법
### 1. kakao developers appkey 발급
https://developers.kakao.com

### 2. project clone
```bash
git clone https://github.com/sehee-lee/kakao_mcp
```

### 3. uv install
```bash
brew install uv
```

### 4. At Claude
아래와 같이 설정
```json
{
  "mcpServers": {
    "kakao search API": {
      "command": "{uv path}",
      "args": [
        "run",
        "python",
        "kakao_mcp/mcp_server.py"
      ],
      "env": {
        "KAKAO_APP_KEY": "{your app key"
      }
    }
  }
}
```