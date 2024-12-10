const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: false, // Disable HTTPS for now
    host: 'localhost',
    port: 8080,
  },
  devServer: {
    proxy: "http://127.0.0.1:8000",
  },
});
