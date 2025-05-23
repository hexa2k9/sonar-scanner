#!/usr/bin/env python3
"""
Edit MediaWiki's PHPUnit junit.xml file.
Based on gist.github.com/black-silence/35b958fe92c704de551a3ca4ea082b87
See https://community.sonarsource.com/t/sonarphp-doesnt-analyze-php-unit-tests-with-dataprovider/2775/5
Copyright (C) 2019 Kosta Harlan <kharlan@wikimedia.org>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import argparse
import xml.etree.ElementTree as etree


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('junit', help='Path to junit.xml')
    args = parser.parse_args()
    tree = etree.parse(args.junit)
    root = tree.getroot()

    for mastersuites in root:
        for suite in mastersuites:
            if 'file' not in suite.attrib:
                continue
            filename = suite.attrib['file']
            for subsuite in suite:
                if subsuite.tag != 'testsuite':
                    continue
                if 'file' not in subsuite.attrib:
                    name = filename
                    for key, value in subsuite.attrib.items():
                        if (key == 'name'):
                            name = value
                    subsuite.attrib['file'] = name

    tree.write(args.junit)


if __name__ == '__main__':
    main()
