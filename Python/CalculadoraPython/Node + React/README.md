# Calculadora 

Projeto frontend e backend feito com React, Webpack e Babel.

## Requisitos
- Node.js instalado
- npm instalado

## Instalação
Abra o terminal na pasta do projeto e execute:

```bash
npm.cmd install
```

## Executar em desenvolvimento

```bash
npm.cmd start
```

A aplicação ficará disponível em http://localhost:3000.

## Gerar versão de produção

```bash
npm.cmd run build
```

Os arquivos de produção serão gerados na pasta `dist`.

## Estrutura

```text
calculadora/
├── public/
│   └── index.html
├── src/
│   ├── App.jsx
│   ├── index.jsx
│   └── style.css
├── package.json
├── webpack.config.js
└── README.md
```

O JSX é processado pelo `babel-loader`, usando `@babel/preset-react`.
