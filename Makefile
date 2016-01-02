PY=python3

BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/public
PUBLISHFILE=$(BASEDIR)/build.py

S3_BUCKET=elliotmarsden.com


publish:
	$(PY) $(PUBLISHFILE)

deploy: publish
	aws s3 sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl public-read --delete
