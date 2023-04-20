# NoSQL

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://riak.com/resources/nosql-databases/" title="NoSQL Databases Explained" target="_blank">NoSQL Databases Explained</a> </li>
<li><a href="https://www.youtube.com/watch?v=qUV2j3XBRHc&ab_channel=Guru99" title="What is NoSQL ?" target="_blank">What is NoSQL ?</a> </li>
<li><a href="https://www.youtube.com/watch?v=E-1xI85Zog8&ab_channel=freeCodeCamp.org" title="MongoDB with Python Crash Course - Tutorial for Beginners" target="_blank">MongoDB with Python Crash Course - Tutorial for Beginners</a> </li>
<li><a href="https://www.youtube.com/watch?v=CB9G5Dvv-EE&ab_channel=DerekBanas" title="MongoDB Tutorial 2 : Insert, Update, Remove, Query" target="_blank">MongoDB Tutorial 2 : Insert, Update, Remove, Query</a> </li>
<li><a href="https://www.mongodb.com/docs/manual/aggregation/" title="Aggregation" target="_blank">Aggregation</a> </li>
<li><a href="https://realpython.com/introduction-to-mongodb-and-python/" title="Introduction to MongoDB and Python" target="_blank">Introduction to MongoDB and Python</a> </li>
<li><a href="https://www.mongodb.com/docs/manual/reference/method/" title="mongo Shell Methods" target="_blank">mongo Shell Methods</a> </li>
<li><a href="https://www.mongodb.com/docs/" title="The mongo Shell" target="_blank">The mongo Shell</a> </li>
</ul>


<h2>Requirements</h2>

<h3>MongoDB Command File</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>MongoDB</code> (version 4.2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be a comment: <code>// my comment</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7) and <code>PyMongo</code> (version 3.10)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.*)</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code></li>
<li>Your code should not be executed when imported (by using <code>if __name__ == "__main__"</code>:)</li>
</ul>

<h2>More Info</h2>

<h3>Install MongoDB 4.2 in Ubuntu 18.04</h3>

<p><a href="https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/" title="Official installation guide" target="_blank">Official installation guide</a></p>

<pre><code>$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" &gt; /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
&gt;&gt;&gt; import pymongo
&gt;&gt;&gt; pymongo.__version__
'3.10.1'
</code></pre>

<p>Potential issue if documents creation doesn’t work or this error: <code>Data directory /data/db not found., terminating</code> (<a href="https://bryantson.medium.com/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479" title="source" target="_blank">source</a> and <a href="https://stackoverflow.com/questions/37702957/mongodb-data-db-not-found" title="source" target="_blank">source</a>)</p>

<pre><code>$ sudo mkdir -p /data/db
</code></pre>

<p>Or if <code>/etc/init.d/mongod</code> is missing, please find here an example of the file:</p>

<details>
<summary>Click to expand/hide file contents</summary>
<pre><code>
#!/bin/sh
### BEGIN INIT INFO
# Provides:          mongod
# Required-Start:    $network $local_fs $remote_fs
# Required-Stop:     $network $local_fs $remote_fs
# Should-Start:      $named
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: An object/document-oriented database
# Description:       MongoDB is a high-performance, open source, schema-free
#                    document-oriented data store that's easy to deploy, manage
#                    and use. It's network accessible, written in C++ and offers
#                    the following features:
#
#                       * Collection oriented storage - easy storage of object-
#                         style data
#                       * Full index support, including on inner objects
#                       * Query profiling
#                       * Replication and fail-over support
#                       * Efficient storage of binary data including large
#                         objects (e.g. videos)
#                       * Automatic partitioning for cloud-level scalability
#
#                    High performance, scalability, and reasonable depth of
#                    functionality are the goals for the project.
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/bin/mongod
DESC=database

NAME=mongod
# Defaults.  Can be overridden by the /etc/default/$NAME
# Other configuration options are located in $CONF file. See here for more:
# http://dochub.mongodb.org/core/configurationoptions
CONF=/etc/mongod.conf
PIDFILE=/var/run/$NAME.pid
ENABLE_MONGOD=yes

# Include mongodb defaults if available.
# All variables set before this point can be overridden by users, by
# setting them directly in the defaults file. Use this to explicitly
# override these values, at your own risk.
if [ -f /etc/default/$NAME ] ; then
        . /etc/default/$NAME
fi

# Handle NUMA access to CPUs (SERVER-3574)
# This verifies the existence of numactl as well as testing that the command works
NUMACTL_ARGS="--interleave=all"
if which numactl &gt;/dev/null 2&gt;/dev/null &amp;&amp; numactl $NUMACTL_ARGS ls / &gt;/dev/null 2&gt;/dev/null
then
    NUMACTL="`which numactl` -- $NUMACTL_ARGS"
    DAEMON_OPTS=${DAEMON_OPTS:-"--config $CONF"}
else
    NUMACTL=""
    DAEMON_OPTS="-- "${DAEMON_OPTS:-"--config $CONF"}
fi


if test ! -x $DAEMON; then
    echo "Could not find $DAEMON"
    exit 0
fi

if test "x$ENABLE_MONGOD" != "xyes"; then
    exit 0
fi

. /lib/lsb/init-functions

STARTTIME=1
DIETIME=10                  # Time to wait for the server to die, in seconds
                            # If this value is set too low you might not
                            # let some servers to die gracefully and
                            # 'restart' will not work

DAEMONUSER=${DAEMONUSER:-mongodb}
DAEMONGROUP=${DAEMONGROUP:-mongodb}

set -e

running_pid() {
# Check if a given process pid's cmdline matches a given name
    pid=$1
    name=$2
    [ -z "$pid" ] &amp;&amp; return 1
    [ ! -d /proc/$pid ] &amp;&amp;  return 1
    cmd=`cat /proc/$pid/cmdline | tr "\000" "\n"|head -n 1 |cut -d : -f 1`
    # Is this the expected server
    [ "$cmd" != "$name" ] &amp;&amp;  return 1
    return 0
}

running() {
# Check if the process is running looking at /proc
# (works for all users)

    # No pidfile, probably no daemon present
    [ ! -f "$PIDFILE" ] &amp;&amp; return 1
    pid=`cat $PIDFILE`
    running_pid $pid $DAEMON || return 1
    return 0
}

start_server() {
            # Start the process using the wrapper
            start-stop-daemon --background --start --quiet --pidfile $PIDFILE \
                        --make-pidfile --chuid $DAEMONUSER:$DAEMONGROUP \
                        --exec $NUMACTL $DAEMON $DAEMON_OPTS
            errcode=$?
        return $errcode
}

stop_server() {
# Stop the process using the wrapper
            start-stop-daemon --stop --quiet --pidfile $PIDFILE \
                        --retry 300 \
                        --user $DAEMONUSER \
                        --exec $DAEMON
            errcode=$?
        return $errcode
}

force_stop() {
# Force the process to die killing it manually
        [ ! -e "$PIDFILE" ] &amp;&amp; return
        if running ; then
                kill -15 $pid
        # Is it really dead?
                sleep "$DIETIME"s
                if running ; then
                        kill -9 $pid
                        sleep "$DIETIME"s
                        if running ; then
                                echo "Cannot kill $NAME (pid=$pid)!"
                                exit 1
                        fi
                fi
        fi
        rm -f $PIDFILE
}


case "$1" in
  start)
        log_daemon_msg "Starting $DESC" "$NAME"
        # Check if it's running first
        if running ;  then
            log_progress_msg "apparently already running"
            log_end_msg 0
            exit 0
        fi
        if start_server ; then
            # NOTE: Some servers might die some time after they start,
            # this code will detect this issue if STARTTIME is set
            # to a reasonable value
            [ -n "$STARTTIME" ] &amp;&amp; sleep $STARTTIME # Wait some time
            if  running ;  then
                # It's ok, the server started and is running
                log_end_msg 0
            else
                # It is not running after we did start
                log_end_msg 1
            fi
        else
            # Either we could not start it
            log_end_msg 1
        fi
        ;;
  stop)
        log_daemon_msg "Stopping $DESC" "$NAME"
        if running ; then
            # Only stop the server if we see it running
                        errcode=0
            stop_server || errcode=$?
            log_end_msg $errcode
        else
            # If it's not running don't do anything
            log_progress_msg "apparently not running"
            log_end_msg 0
            exit 0
        fi
        ;;
  force-stop)
        # First try to stop gracefully the program
        $0 stop
        if running; then
            # If it's still running try to kill it more forcefully
            log_daemon_msg "Stopping (force) $DESC" "$NAME"
                        errcode=0
            force_stop || errcode=$?
            log_end_msg $errcode
        fi
        ;;
  restart|force-reload)
        log_daemon_msg "Restarting $DESC" "$NAME"
                errcode=0
        stop_server || errcode=$?
        # Wait some sensible amount, some server need this
        [ -n "$DIETIME" ] &amp;&amp; sleep $DIETIME
        start_server || errcode=$?
        [ -n "$STARTTIME" ] &amp;&amp; sleep $STARTTIME
        running || errcode=$?
        log_end_msg $errcode
        ;;
  status)

        log_daemon_msg "Checking status of $DESC" "$NAME"
        if running ;  then
            log_progress_msg "running"
            log_end_msg 0
        else
            log_progress_msg "apparently not running"
            log_end_msg 1
            exit 1
        fi
        ;;
  # MongoDB can't reload its configuration.
  reload)
        log_warning_msg "Reloading $NAME daemon: not implemented, as the daemon"
        log_warning_msg "cannot re-read the config file (use restart)."
        ;;

  *)
        N=/etc/init.d/$NAME
        echo "Usage: $N {start|stop|force-stop|restart|force-reload|status}" &gt;&amp;2
        exit 1
        ;;
esac

exit 0
    </code></pre>
    </details>

<h3>Use “container-on-demand” to run MongoDB</h3>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - MongoDB</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MongoDB before playing with it:</li>
</ul>

<pre><code>$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&amp;gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
</code></pre>

  </div>
</div>