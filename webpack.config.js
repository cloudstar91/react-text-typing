var path = require('path');
var node_modules = path.resolve(__dirname, 'node_modules');
var minifiedReact = path.resolve(node_modules, 'react/dist/react.min.js');

var config = {
  entry: ['./src/app.jsx'],

  // Use minified react for quicker rebundling.
  // No propTypes type validation. Also lose error messages
  // resolve: {
  //   alias: {
  //     'react': minifiedReact
  //   }
  // },

  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js'
  },

  module: {
    loaders: [
      {
        test: /\.jsx$/,
        loader: 'jsx-loader'
      },
      {
        test: /\.scss$/,
        loader: 'style!css!sass'
      },
      {
        test: /\.css$/,
        loader: 'style!css'
      },
      {
        // proxima-nova
        test: /\.(woff|ttf)$/,
        loader: 'url?limit=100000'
      },
      {
        test: /\.eot$/,
        loader: "file-loader"
      },
      {
        test: /\.(woff|woff2|ttf|otf|eot|svg)(\?.+)$/,
        loader: 'url?limit=100000'
      }
    ],

    // stop webpack from parsing the minified file
    // noParse: [minifiedReact]
  },

};

if (process.env.NODE_ENV === "development") {
  config.entry.push('webpack/hot/dev-server');
}

module.exports = config;
