#!/usr/bin/env python
from conanos.build import Main

if __name__ == "__main__":
    Main('gst-plugins-ugly',pure_c=True)