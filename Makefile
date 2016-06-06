PY=python3

BASE_DIR=$(CURDIR)
OUTPUT_DIR=$(BASE_DIR)/public
PUBLISH_FILE=$(BASE_DIR)/build.py

S3_BUCKET=elliotmarsden.com

publish:
	$(PY) $(PUBLISH_FILE)

deploy: publish
	aws s3 sync $(OUTPUT_DIR)/ s3://$(S3_BUCKET) --acl public-read --delete
