:mod:`robotics <pybricks.robotics>` -- ロボティクスとドライブベース
===========================================================================

.. automodule:: pybricks.robotics
    :no-members:

.. pybricks-requirements::

.. blockimg:: pybricks_variables_set_drive_base

.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: 指定した距離や角度だけ動かす

    以下のコマンドを使用して、指定した距離だけ走行したり、指定した角度
    だけ旋回したりします。

    これらは内部の回転センサーを使って測定されます。走行中にホイールが
    滑ることがあるため、走行距離と角度は推定値にすぎません。

    .. blockimg:: pybricks_blockDriveBaseMove_drivebase_move_straight

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. blockimg:: pybricks_blockDriveBaseMove_drivebase_move_turn_by

    .. blockimg:: pybricks_blockDriveBaseMove_drivebase_move_turn_to

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. blockimg:: pybricks_blockDriveBaseMove_drivebase_move_arc_deg

    .. blockimg:: pybricks_blockDriveBaseMove_drivebase_move_arc_mm

    .. automethod:: pybricks.robotics.DriveBase.arc

    .. pybricks-requirements:: stm32-float

    .. blockimg:: pybricks_blockDriveBaseMove_drivebase_move_coordinates

    .. automethod:: pybricks.robotics.DriveBase.move_by

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_straight_speed

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_straight_acceleration

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_turn_rate

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_turn_acceleration

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. automethod:: pybricks.robotics.DriveBase.done

    .. rubric:: 走り続ける

    :meth:`.drive` を使用して、目的の速度とステアリングで走行を開始します。

    :meth:`.stop` を使うか、再度 :meth:`.drive` を使って進路を変えるまで
    走り続けます。たとえば、センサーが反応するまで走行し、その後
    停止したり向きを変えたりできます。

    .. blockimg:: pybricks_blockDriveBaseStart

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. blockimg:: pybricks_blockDriveBaseStop_coast

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. blockimg:: pybricks_blockDriveBaseStop_brake

    .. automethod:: pybricks.robotics.DriveBase.brake

    .. blockimg:: pybricks_blockDriveBaseStop_hold

    .. automethod:: pybricks.robotics.DriveBase.hold

    .. rubric:: 計測

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_distance

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_angle

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_speed

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_turn_rate

    .. automethod:: pybricks.robotics.DriveBase.state

    .. versionchanged:: 3.6

        ドライブベースを停止するようになりました。ゼロ以外の値を
        使用できるようになりました。

    .. blockimg:: pybricks_blockDriveBaseResetWithValues

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. automethod:: pybricks.robotics.DriveBase.stalled

    .. pybricks-requirements:: gyro

    .. rubric:: ジャイロでの走行

    .. blockimg:: pybricks_blockDriveBaseUseGyro

    .. automethod:: pybricks.robotics.DriveBase.use_gyro

    ハブがロボットに平らに取り付けられていない場合は、
    :class:`PrimeHub() <pybricks.hubs.PrimeHub>` 、
    :class:`InventorHub() <pybricks.hubs.PrimeHub>` 、
    :class:`EssentialHub() <pybricks.hubs.EssentialHub>` 、または
    :class:`TechnicHub() <pybricks.hubs.TechnicHub>` を初期化するときに
    ``top_side`` と ``front_side`` のパラメータを必ず指定してください。
    これにより、ロボットは旋回時にどの回転を測定すべきかを認識します。

    各ハブのジャイロは少しずつ異なるため、大きな旋回や同じ方向への
    多数の小さな旋回では、数度ずれることがあります。たとえば、ロボットを
    1回転させるには :meth:`turn(357) <pybricks.robotics.DriveBase.turn>` や
    :meth:`turn(362) <pybricks.robotics.DriveBase.turn>` を使う必要が
    あるかもしれません。

    デフォルトでは、このクラスは移動の完了後もロボットの位置を維持
    しようとします。つまり、方位角を維持しようとして、ロボットを
    持ち上げるとホイールが回転します。これを避けるには、最後の
    :meth:`straight <pybricks.robotics.DriveBase.straight>` 、
    :meth:`turn <pybricks.robotics.DriveBase.turn>` 、または
    :meth:`arc <pybricks.robotics.DriveBase.arc>` コマンドで
    ``then=Stop.COAST`` を選択します。

    .. _measuring:

    .. rubric:: ロボットの寸法の測定と検証

    最初の推定値として、 ``wheel_diameter`` と ``axle_track`` を定規で
    測定できます。ホイールが実際に地面に接する場所は分かりにくいため、
    ``axle_track`` は両ホイールの中点同士の距離として推定できます。

    定規がない場合は、LEGOビームを使って測定できます。穴の中心同士の
    距離は8 mmです。タイヤによっては、側面に直径が印刷されています。
    たとえば、62.4 x 20は直径が62.4 mmで幅が20 mmであることを意味します。

    実際には、ほとんどのホイールはロボットの重みでわずかに押しつぶされます。
    確認するには、 ``my_robot.straight(1000)`` を使ってロボットを
    1000 mm走行させ、実際にどれだけ進んだかを測定します。
    次のように補正します。

        - ロボットが **十分に進まない** 場合は、 ``wheel_diameter`` の値を
          わずかに **小さく** します。
        - ロボットが **進みすぎる** 場合は、 ``wheel_diameter`` の値を
          わずかに **大きく** します。

    モーターのシャフトとアクスルはロボットの荷重でわずかに曲がり、
    ホイールの接地点がロボットの中点に近づきます。確認するには、
    ``my_robot.turn(360)`` を使ってロボットを360度旋回させ、
    元の場所に戻っているかを確認します。

        - ロボットの旋回が **足りない** 場合は、 ``axle_track`` の値を
          わずかに **大きく** します。
        - ロボットの旋回が **大きすぎる** 場合は、 ``axle_track`` の値を
          わずかに **小さく** します。

    これらの調整を行うときは、上記のように必ず ``wheel_diameter`` から
    調整してください。完了後は、旋回と直進の両方を必ずテストしてください。

    .. rubric:: DriveBaseのモーターを個別に使用する

    :class:`.DriveBase` オブジェクトを作成した後でも、その2つのモーターを
    個別に使用できます。一方のモーターを開始すると、もう一方のモーターは
    自動的に停止します。同様に、モーターがすでに動作中にドライブベースを
    動かすと、元の動作はキャンセルされ、ドライブベースが引き継ぎます。

    .. rubric:: 高度な設定

    :meth:`.settings` メソッドは、直進動作と旋回のデフォルトの速度や
    加速度など、よく使われる設定を調整するために使用します。
    より高度な制御設定を調整するには、以下の属性を使用します。

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:

    .. versionchanged:: 3.2

        :meth:`done` と :meth:`stalled` の各メソッドは移動しました。

.. pybricks-requirements::

.. blockimg:: pybricks_variables_set_car

.. versionadded:: 3.4

.. autoclass:: pybricks.robotics.Car
    :no-members:

    .. blockimg:: pybricks_blockCarSteer

    .. automethod:: pybricks.robotics.Car.steer

    .. blockimg:: pybricks_blockCarDrive_car_drive_at_power

    .. automethod:: pybricks.robotics.Car.drive_power

    .. blockimg:: pybricks_blockCarDrive_car_drive_at_speed

    .. automethod:: pybricks.robotics.Car.drive_speed

例
-------------------

ドライブベースで直進してその場で旋回する
********************************************************

このプログラムは、走行と旋回の基本を示しています。

.. literalinclude::
    ../../examples/pup/robotics/drivebase_basics.py

前輪ステアリングの車をリモートコントロールする
**************************************************

このプログラムは、 :class:`リモートコントロール <pybricks.pupdevices.Remote>`
を使って前輪ステアリングの車を走行させる方法を示しています。

このプログラムでは、ポートは `LEGO Technic 42099 Off-Roader
<https://pybricks.com/projects/sets/technic/42099-off-roader/>`_ のものに
一致していますが、前輪ステアリングの他の車でも使用できます。車両に
駆動モーターが1つしかない場合は、以下で使用しているモーターのタプルの
代わりに、単一のモーターを使用できます。

.. literalinclude::
    ../../examples/pup/robotics/car_remote.py
