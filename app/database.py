from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import boto3

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get("CREDENTIALS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("CREDENTIALS_SECRET_KEY"),
    region_name="ap-northeast-3"
)

s3_url = os.environ.get("AWS_S3_URL")

s3_bucket_name = os.environ.get("AWS_S3_BUCKET_NAME")