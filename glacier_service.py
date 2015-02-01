__author__ = 'igorkhomenko'

from boto.glacier.layer1 import Layer1
from boto.glacier.concurrent import ConcurrentUploader

target_vault_name = 'backups'
region_name = "ap-southeast-2"

def upload_archive(file_name):
    glacier_layer1 = Layer1(region_name=region_name)

    uploader = ConcurrentUploader(glacier_layer1, target_vault_name, 32*1024*1024)

    print("operation starting...")

    archive_id = uploader.upload(file_name, file_name)

    print("Success! archive id: '%s'" % archive_id)

def delete_archive(archive_id):
    glacier_layer1 = Layer1(region_name=region_name)

    print("operation starting...")

    print glacier_layer1.delete_archive(target_vault_name, archive_id)

def get_vault_metadata():
    glacier_layer1 = Layer1(region_name=region_name)

    print("operation starting...")

    vault_metadata = glacier_layer1.describe_vault(target_vault_name)

    print("Success! vault metadata: %s" % vault_metadata)

def list_jobs(job_id=None):
    glacier_layer1 = Layer1(region_name=region_name)

    print("operation starting...")

    if(job_id != None):
        print glacier_layer1.get_job_output(target_vault_name, job_id)
    else:
        output =  glacier_layer1.list_jobs(target_vault_name, completed=False)
        print output

def get_vault_inventory():
    glacier_layer1 = Layer1(region_name=region_name)

    print("operation starting...")

    job_id = glacier_layer1.initiate_job(target_vault_name, {"Description":"inventory-job",
                                                             "Type":"inventory-retrieval", "Format":"JSON"})

    print("Success! inventory job id: %s" % (job_id,))


if __name__ == '__main__':
    # upload_archive("Hadoop.zip")
    # get_vault_inventory()
    # get_vault_metadata()
    list_jobs()