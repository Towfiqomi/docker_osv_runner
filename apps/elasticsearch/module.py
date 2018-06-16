default = api.run(
' --cwd=/elasticsearch /java.so '
' -Xms1g -Xmx1g -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+AlwaysPreTouch -Xss1m '
' -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djna.nosys=true -XX:-OmitStackTraceInFastThrow '
' -Dio.netty.noUnsafe=true -Dio.netty.noKeySetOptimization=true -Dio.netty.recycler.maxCapacityPerThread=0 '
' -Dlog4j.shutdownHookEnabled=false -Dlog4j2.disable.jmx=true -XX:+HeapDumpOnOutOfMemoryError '
' -Des.enforce.bootstrap.checks=true '
' -Des.path.home=/elasticsearch '
' -Des.path.conf=/elasticsearch/config '
' -Des.distribution.flavor=oss -Des.distribution.type=tar '
' -cp /elasticsearch/lib/* '
' org.elasticsearch.bootstrap.Elasticsearch' )
