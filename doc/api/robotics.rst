:mod:`robotics <pybricks.robotics>` -- ロボティクス
===========================================================

.. automodule:: pybricks.robotics
    :no-members:


.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: 指定した距離や角度だけ動かす

    次のコマンドを使うと、指定した距離だけ走行したり、指定した角度だけ
    旋回したりできます。

    これは内蔵の回転センサーで測定されます。走行中にホイールが滑ることが
    あるため、走行距離と角度は推定値です。

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. rubric:: 走り続ける

    :meth:`.drive` を使うと、指定した速度と操舵で走行を開始します。

    :meth:`.stop` を使うか、 :meth:`.drive` を再度使って進路を変更する
    まで走り続けます。たとえば、センサーが反応するまで走行させてから、
    停止したり方向転換したりできます。

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. rubric:: 計測

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. automethod:: pybricks.robotics.DriveBase.state

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. rubric:: ロボットの寸法の測定と検証

    最初の推定値として、 ``wheel_diameter`` と
    ``axle_track`` を定規で測定できます。ホイールが実際に地面に接する
    位置は分かりにくいため、 ``axle_track`` は両ホイールの中点同士の
    距離として推定できます。

    実際には、ほとんどのホイールはロボットの重みでわずかに潰れます。
    確認するには、 ``my_robot.straight(1000)`` でロボットを1000 mm
    走行させ、実際にどれだけ進んだかを測ります。次のように補正します。

        - ロボットが **十分に進まない** 場合は、 ``wheel_diameter`` の
          値をわずかに **小さく** します。
        - ロボットが **進みすぎる** 場合は、 ``wheel_diameter`` の値を
          わずかに **大きく** します。

    モーターのシャフトとアクスルはロボットの荷重でわずかに曲がり、
    ホイールの接地点がロボットの中点に近づきます。確認するには、
    ``my_robot.turn(360)`` でロボットを360度旋回させ、同じ位置に
    戻るかをチェックします。

        - ロボットが **十分に回らない** 場合は、 ``axle_track`` の値を
          わずかに **大きく** します。
        - ロボットが **回りすぎる** 場合は、 ``axle_track`` の値を
          わずかに **小さく** します。

    これらの調整を行うときは、上記のように必ず
    ``wheel_diameter`` を先に調整してください。終わったら、
    旋回と直進の両方を必ずテストします。

    .. rubric:: DriveBaseのモーターを個別に使用する

    ``left_motor`` と ``right_motor`` という2つの ``Motor`` オブジェクトを
    使って :class:`.DriveBase` オブジェクトを作ったとします。
    DriveBaseが **アクティブ** な間は、これらのモーターを個別に
    使用 **できません** 。

    DriveBaseは走行中だけでなく、 :meth:`.straight` や
    :meth:`.turn` コマンドの後に
    ホイールをその場でアクティブに保持している間もアクティブです。
    :class:`.DriveBase` を無効にするには、 :meth:`.stop` を呼び出します。


    .. rubric:: 高度な設定

    :meth:`.settings` メソッドは、
    直進動作と旋回の既定の速度や加速度のような、よく使う設定を調整する
    ために使われます。
    より高度な制御設定を調整するには、次の属性を使用します。

    設定はロボットが停止しているときにのみ変更できます。
    つまり走行を開始する前か、 :meth:`.stop` を呼び出した後です。

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:
