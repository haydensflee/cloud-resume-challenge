.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec hayden --no-session -- sam deploy --no-confirm-changeset

deploy-site:
	aws-vault exec hayden --no-session -- aws s3 sync ./resume-site s3://my-fantastic-website-hl

invoke-get:
	sam build && aws-vault exec hayden --no-session -- sam local invoke GetFunction

invoke-put:
	sam build && aws-vault exec hayden --no-session -- sam local invoke PutFunction