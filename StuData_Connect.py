#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")
cursor = conn.cursor()