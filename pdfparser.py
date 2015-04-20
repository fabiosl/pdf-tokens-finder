#-*- encoding: utf-8 -*-
import subprocess
from nltk.tokenize import RegexpTokenizer
import glob

tokenizer = RegexpTokenizer(r'\w+')
dictionary = {}

target_tokens = ["oracle", "mysql", "microsoft sql server", "mongodb", "postgresql", "db2", "microsoft access", "cassandra", "sqlite", "redis", "sap adaptive server", "solr", "teradata", "elasticsearch", "hbase", "filemaker", "hive", "splunk", "informix", "memcached", "sap hana", "neo4j", "couchdb", "couchbase", "mariadb", "firebird", "netezza", "microsoft azure sql database<", "vertica", "amazon dynamodb", "riak", "dbase", "marklogic", "ingres", "sphinx", "greenplum", "endeca", "ehcache", "ravendb", "hazelcast", "interbase", "sap iq", "amazon redshift", "sap sql anywhere", "hypersql", "adabas", "msql", "impala", "derby", "jackrabbit", "cloudant", "google bigquery", "h2", "berkeley db", "google search appliance", "gemfire", "titan", "maxdb", "orientdb", "oracle coherence", "amazon simpledb", "accumulo", "unidata,universe", "timesten", "virtuoso", "sap advantage database server", "aerospike", "caché", "oracle nosql", "openedge", "db4o", "infinispan", "teradata aster", "amazon cloudsearch", "enterprisedb", "rethinkdb", "ims", "drizzle", "leveldb", "jena", "datameer", "versant object database", "percona server", "voltdb", "infobright", "datomic", "sesame", "influxdb", "paraccel", "oracle rdb", "idms", "sqlbase", "d3", "nuodb", "sedna", "objectstore", "foundationdb", "memsql", "mnesia", "jbase", "gridgain", "arangodb", "monetdb", "empress", "dataease", "sparksee", "basex", "apache drill", "kdb+", "red brick", "model 204", "amazon aurora", "pouchdb", "giraph", "microsoft azure documentdb</a><", "altibase", "google cloud datastore", "allegrograph", "nonstop sql", "r:base", "microsoft azure search", "datacom/db", "soliddb", "zodb", "hypertable", "vectorwise", "gt.m", "clustrix", "objectivity/db", "tokudb", "1010data", "infinidb", "xapian", "pervasive psql", "algebraix", "cloudkit", "kognitio", "frontbase", "tokyo cabinet", "hadapt", "tokumx", "vistadb", "northgate reality", "ncache", "openbase", "exasol", "tamino", "nexusdb", "wiredtiger", "websphere extreme scale", "gemstone/s", "rainstor", "objectdb", "scidb", "tokyo tyrant", "cubrid", "infinitegraph", "project voldemort", "indica", "ittia", "exist-db", "xap", "openinsight", "perst", "extremedb", "sqrrl", "hibari", "rocksdb", "scimoredb", "splice machine", "compass", "akiban", "mimer sql", "xtremedata", "mapdb", "stardog", "infogrid", "dataupia", "graphdb", "luciddb", "webscalesql", "clusterpoint", "crate.io", "stsdb", "sql.js", "flockdb", "scalaris", "scalebase", "redland", "modeshape", "strabon", "redstore", "4store", "searchblox", "terrastore", "kyoto cabinet", "scaledb", "eloquera", "hamsterdb", "siaqodb", "hypergraphdb", "rasdaman", "transbase", "geniedb", "hyperdex", "starcounter", "elliptics", "openqm", "dbsight", "translattice", "lightcloud", "kyoto tycoon", "velocitydb", "brightstardb", "smallsql", "versant fastobjects", "cubicweb", "jade", "dydra", "scaleout stateserver", "c-treeace", "tajo", "amisa server", "bangdb", "bergdb", "blazegraph", "codernitydb", "cortexdb", "densodb", "djondb", "ejdb", "event store", "exorbyte", "fleetdb", "globalsdb", "graphbase", "hyperleveldb", "jasdb", "jethrodata", "justonedb", "ledisdb", "lokijs", "mulgara", "nanolat", "neventstore", "origodb", "postgres-xl", "raptordb", "resin cache", "senseidb", "sequoiadb", "sisodb", "sparkledb", "srch²", "tarantool", "tomp2p", "velocitygraph", "wakandadb", "whitedb"]

def read_pdf_file(filename):
	print "Reading %s..." % filename
	cmd = "/Users/fabiosl/Downloads/pdfminer-20140328/tools/pdf2txt.py %s" % filename
	p = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	out, err = p.communicate()
	print "Finished reading %s..." % filename 
	return out.lower

for filename in glob.glob("/Users/fabiosl/Desktop/papers/*.pdf"):
	out = read_pdf_file(filename)

	document_tokens = tokenizer.tokenize(out)
	for token in target_tokens:
		occur = document_tokens.count(token)
		if occur: 
			if token in dictionary:
				dictionary[token] = dictionary[token] + occur
			else:
				dictionary[token] = occur

	print dictionary