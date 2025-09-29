# Puqee官网

本目录包含Puqee项目的官方网站静态文件。

## 目录结构

```
web/
├── site/          # 官网静态文件
│   └── index.html # 官网主页
└── chat/          # 聊天界面文件
    ├── static/    # 聊天界面的CSS、JS等静态文件
    └── templates/ # 聊天界面的HTML模板
```

## 运行官网

### 使用Python内置服务器
```bash
cd web/site
python -m http.server 3000
```
然后在浏览器中访问：http://localhost:3000

### 使用其他静态文件服务器
您可以使用任何静态文件服务器来服务 `web/site/` 目录中的文件。

## 部署

官网是纯静态网站，可以部署到：
- GitHub Pages
- Vercel
- Netlify
- 其他静态网站托管服务

## 聊天界面

聊天界面文件位于 `web/chat/` 目录，需要Python后端支持运行。

## 开发说明

- 官网文件完全独立，不依赖Python后端
- 可以直接在浏览器中打开 `web/site/index.html` 文件预览
- 聊天界面需要Python后端支持