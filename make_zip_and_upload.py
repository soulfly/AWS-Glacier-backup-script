__author__ = 'igorkhomenko'

import os
import zipfile
import datetime

from glacier_service import GlacierService

def zip_dir(dir_path, zf):
    for dirname, subdirs, files in os.walk(dir_path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))

if __name__ == '__main__':
    datetime = datetime.datetime.utcnow().isoformat().replace(":", "_").replace("-", "_").replace(".", "_")

    archive_name = 'backup_%s.zip' % datetime

    print archive_name

    # prepare archive
    zipf = zipfile.ZipFile(archive_name, 'w')
    zip_dir('test_dir1', zipf) # replace with real dirs/files
    zipf.close()

    # upload
    glacier = GlacierService("backups", "ap-southeast-2")
    glacier.upload_archive(archive_name)

    # cleanup
    os.remove(archive_name)


