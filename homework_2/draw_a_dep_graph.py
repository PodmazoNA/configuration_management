import os
import requests
import xml.etree.ElementTree as ET
import graphviz
from PIL import Image
import sys

def download_pom(pom_url):
    str1 = pom_url.replace("github.com", "raw.githubusercontent.com") + "/refs/heads/master/pom.xml"
    filename = os.path.basename(str1)
    response = requests.get(str1)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print("ERROR")

def find_dep(pom_path):
    try:
        tree = ET.parse(pom_path)
        root = tree.getroot()
        namespace = {'maven': 'http://maven.apache.org/POM/4.0.0'}
        dependencies = root.findall('.//maven:dependency', namespaces=namespace)
        dependencies_list = []
        for dependency in dependencies:
            group_id = dependency.find('maven:groupId', namespaces=namespace).text
            artifact_id = dependency.find('maven:artifactId', namespaces=namespace).text
            version = dependency.find('maven:version', namespaces=namespace).text
            dependencies_list.append({'groupId': group_id, 'artifactId': artifact_id, 'version': version})
        return dependencies_list
    except Exception as e:
        print(f"Error: {pom_path}: {e}")
        return []

def vis_dep(name, dep_list):
    dot = graphviz.Digraph(format='png')
    dot.node(name)
    for elem in dep_list:
        dot.node(elem['groupId'])
        dot.edge(name, elem['groupId'])

    dot.render(name + '_dep_graph', view=True)

if __name__ == "__main__":
    name = sys.argv[1]
    path = sys.argv[2]
    download_pom(path)
    dep = find_dep("pom.xml")
    os.remove("pom.xml")
    vis_dep(name, dep)
    os.system(f'open {name + "_dep_graph.png"}')
