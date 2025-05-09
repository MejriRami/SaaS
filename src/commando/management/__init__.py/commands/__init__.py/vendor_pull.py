from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand
import helpers

from pathlib import Path

# Ensure the directory path is a Path object
STATICFILES_VENDOR_DIR = Path(getattr(settings, 'STATICFILES_VENDOR_DIR', 'static/vendor'))

# Dictionary to store vendor files and their URLs
VENDOR_STATICFILES = {
    # 'filename.js': 'https://example.com/path/to/filename.js',
}

class Command(BaseCommand):
    help = "Download vendor static files"

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files...")
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)

            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("All vendor static files downloaded successfully.")
            )
        else:
            self.stdout.write(
                self.style.ERROR("Failed to download all vendor static files.")
            )
