# -*- coding: utf-8 -*-
import chardet
import os

class Utils:
    def detect_encoding(self, path):
        with open(os.path.join(path, os.listdir(path)[0]), "rb") as file_data:
            data = file_data.read()
        return chardet.detect(data)

    @staticmethod
    def create_directorys():
        """
        This function generates the needed directorys, if they are missing.
        """
        print(":: Check if all directorys are present")
        if not os.path.exists("input"):
            os.makedirs("input")
            print("\t:: Created input directory")
            return True
        if not os.path.exists("database"):
            os.makedirs("database")
            print("\t:: Created database directory")
        return False
