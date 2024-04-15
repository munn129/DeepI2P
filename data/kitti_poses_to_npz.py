# writer: moon
# I can not find file which makes poses text to npz file.
# So, I made it.

import os
import numpy as np

def read_txt_pose(file_path):
    poses = []
    with open(file_path, 'r') as file:
        for line in file:
            # 한 줄씩 읽어들여 공백을 기준으로 분리한 후에 float으로 변환하여 리스트에 추가
            pose = [float(x) for x in line.split()]
            # 1차원 리스트를 3x4 행렬로 변환
            pose_matrix_3x4 = np.array(pose).reshape(3, 4)
            # 4x4 행렬로 변환하기 위해 마지막 행에 [0, 0, 0, 1] 추가
            pose_matrix_4x4 = np.vstack([pose_matrix_3x4, [0, 0, 0, 1]])
            poses.append(pose_matrix_4x4)
    return poses

def save_npz_poses(poses, output_dir):
    for i, pose in enumerate(poses):
        # npz 파일 이름을 생성
        npz_file = f"{output_dir}/{i:06d}.npz"
        # npz 파일에 pose 행렬을 저장
        np.savez(npz_file, pose=pose)

def main():
    txt_directory = "../datasets/kitti/poses"
    output_directory = "../datasets/kitti/poses_npz"

    txt_paths = []
    output_paths = []
    for i in range(11):
        txt_paths.append(f'{txt_directory}/{i:02d}.txt')
        output_paths.append(f'{output_directory}/{i:02d}')

    for txt_file, save_dir in zip(txt_paths, output_paths):
        poses = read_txt_pose(txt_file)
        save_npz_poses(poses, save_dir)

if __name__ == "__main__":
    main()
