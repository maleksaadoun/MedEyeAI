# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config({
  extends: [
    // Remove ...tseslint.configs.recommended and replace with this
    ...tseslint.configs.recommendedTypeChecked,
    // Alternatively, use this for stricter rules
    ...tseslint.configs.strictTypeChecked,
    // Optionally, add this for stylistic rules
    ...tseslint.configs.stylisticTypeChecked,
  ],
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config({
  plugins: {
    // Add the react-x and react-dom plugins
    'react-x': reactX,
    'react-dom': reactDom,
  },
  rules: {
    // other rules...
    // Enable its recommended typescript rules
    ...reactX.configs['recommended-typescript'].rules,
    ...reactDom.configs.recommended.rules,
  },
})

```
med-eye-ai
├─ eslint.config.js
├─ index.html
├─ package-lock.json
├─ package.json
├─ README.md
├─ src
│  ├─ api
│  │  ├─ adminService.ts
│  │  ├─ authService.ts
│  │  ├─ axios.ts
│  │  └─ userService.ts
│  ├─ App.css
│  ├─ App.tsx
│  ├─ assets
│  │  ├─ bg1.jpg
│  │  ├─ flags
│  │  │  ├─ Jordan_flag_icon_round.svg
│  │  │  └─ UK_flag_icon_round.svg
│  │  ├─ logo.png
│  │  ├─ macro-eye-iris.jpg
│  │  ├─ new-logo.png
│  │  ├─ react.svg
│  │  └─ team
│  │     ├─ amer.jpeg
│  │     ├─ hala.jpeg
│  │     ├─ layan4.jpeg
│  │     └─ malek.jpeg
│  ├─ enums
│  │  └─ userRole.ts
│  ├─ i18n
│  │  ├─ ar.json
│  │  ├─ en.json
│  │  └─ i18n.ts
│  ├─ index.css
│  ├─ main.tsx
│  ├─ pages
│  │  ├─ admin
│  │  │  ├─ home
│  │  │  │  └─ admin-home.tsx
│  │  │  ├─ recommendations-management
│  │  │  │  └─ recommendations-management.tsx
│  │  │  └─ users
│  │  │     ├─ user-details
│  │  │     │  └─ user-details.tsx
│  │  │     └─ users-management.tsx
│  │  ├─ client
│  │  │  ├─ contact
│  │  │  │  └─ contact.tsx
│  │  │  ├─ history
│  │  │  │  └─ history.tsx
│  │  │  └─ home
│  │  │     └─ home.tsx
│  │  ├─ landing-page
│  │  │  ├─ landing-page.tsx
│  │  │  └─ sections
│  │  │     ├─ contact-section
│  │  │     │  └─ contact-section.tsx
│  │  │     ├─ login-section
│  │  │     │  └─ login-section.tsx
│  │  │     ├─ main-section
│  │  │     │  └─ main-section.tsx
│  │  │     └─ register-section
│  │  │        └─ register-section.tsx
│  │  ├─ not-found
│  │  │  └─ not-found.tsx
│  │  └─ profile
│  │     └─ profile.tsx
│  ├─ Routes
│  │  ├─ layout
│  │  │  └─ logedin-layout.tsx
│  │  └─ Rotes
│  │     └─ Routes.tsx
│  ├─ shared
│  │  └─ my-card.tsx
│  └─ vite-env.d.ts
├─ tsconfig.app.json
├─ tsconfig.json
├─ tsconfig.node.json
└─ vite.config.ts

```