module.exports = {
  publicPath: '/',
  configureWebpack: {
    output: {
      filename: 'js/[name].js',
      chunkFilename: 'js/[name].js',
    }
  },
  chainWebpack: config => {
    config.plugin('extract-css').tap(args => {
      args[0].filename = 'css/[name].css';
      args[0].chunkFilename = 'css/[name].css';
      return args;
    });
  }
};