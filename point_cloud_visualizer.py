import open3d as o3d
import numpy as np

print("Load a ply point cloud, print it, and render it")

point_cloud_path = "data/sample_office_scene.ply" # Change this to your file path
pcd = o3d.io.read_point_cloud(point_cloud_path)
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412)