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

    def load_file_to_db(self, path, encoding, db, timestamp):
        return path

    def load_files(self, path, encoding, db, timestamp):
        files_to_load = []
        for x in os.walk(path):
            files_to_load.extend(self.get_files_of_dir(x[0]))
        #print(files_to_load)


    def get_files_of_dir(self, path):
        files = []
        for file in os.listdir(path):
            files.append(os.path.join(path, file))
        return files
