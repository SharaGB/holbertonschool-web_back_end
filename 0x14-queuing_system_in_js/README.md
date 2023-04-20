# Queuing System in JS

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://user-images.githubusercontent.com/90220978/233509803-664586a8-15bd-47b3-9bc1-3325f7556544.png" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://redis.io/docs/getting-started/" title="Redis quick start" target="_blank">Redis quick start</a></li>
<li><a href="https://redis.io/docs/ui/cli/" title="Redis client interface" target="_blank">Redis client interface</a></li>
<li><a href="https://github.com/redis/node-redis" title="Redis client for Node JS" target="_blank">Redis client for Node JS</a></li>
<li><a href="https://github.com/Automattic/kue" title="Kue" target="_blank">Kue</a> <em>deprecated but still use in the industry</em></li>
</ul>


<h2>Requirements</h2>

<ul>
<li>All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7</li>
<li>All of your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
</ul>

<h2>Required Files for the Project</h2>

<h3><code>package.json</code></h3>

<details>
<summary>
Click to show/hide file contents</summary>
<pre><code>
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
</code>
</pre>
</details>

<h3><code>.babelrc</code></h3>

<details>
<summary>
Click to show/hide file contents
</summary>
<pre><code> 
{
  "presets": [
    "@babel/preset-env"
  ]
}
</code>
</pre>
</details>

<h3>and…</h3>

<p>Don’t forget to run <code>$ npm install</code> when you have the <code>package.json</code></p>

  </div>
</div>
