from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task

# 全デバイスをセットアップする。
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)
gripper = Motor(Port.C)
drive_base = DriveBase(left, right, 56, 114)


# グリッパーを上下に動かす。
async def move_gripper():
    await gripper.run_angle(500, -90)
    await gripper.run_angle(500, 90)


# 前進しながら、旋回とグリッパー動作を同時に行い、後進する。
async def main():
    await drive_base.straight(250)
    await multitask(drive_base.turn(90), move_gripper())
    await drive_base.straight(-250)


# メインのプログラムを最初から最後まで実行する。
run_task(main())
