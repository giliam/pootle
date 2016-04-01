module.exports = {
  'extends': 'airbnb',
  env: {
    browser: true,
  },
  parserOptions: {
    ecmaVersion: 6,
    ecmaFeatures: {
      jsx: true,
    },
    sourceType: 'module',
  },
  globals: {
    gettext: false,
    ngettext: false,
    interpolate: false,
    l: false,
    PTL: false,
    require: false,
    shortcut: false,
    sorttable: false,
  },
  plugins: [
    'react',
  ],
};
