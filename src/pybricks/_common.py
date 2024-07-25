# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Generic cross-platform module for typical devices like lights, displays,
speakers, and batteries."""

from __future__ import annotations

from typing import (
    Union,
    Iterable,
    overload,
    Optional,
    Tuple,
    Collection,
    Set,
    TYPE_CHECKING,
)

from .tools import Matrix
from .parameters import Axis, Direction, Stop, Button, Port, Color, Side

if TYPE_CHECKING:
    from typing import Any, Awaitable, TypeVar

    from .parameters import Number

    _T_co = TypeVar("_T_co", covariant=True)

    class MaybeAwaitable(None, Awaitable[None]): ...

    # HACK: Cannot subclass bool, so using Any instead.
    class MaybeAwaitableBool(Any, Awaitable[bool]): ...

    class MaybeAwaitableFloat(float, Awaitable[float]): ...

    class MaybeAwaitableInt(int, Awaitable[int]): ...

    class MaybeAwaitableTuple(Tuple[_T_co], Awaitable[Tuple[_T_co]]): ...

    class MaybeAwaitableColor(Color, Awaitable[Color]): ...


class System:
    """System control actions for a hub."""

    def set_stop_button(
        self, button: Optional[Union[Button, Iterable[Button]]]
    ) -> None:
        """
        set_stop_button(button)

        実行中のスクリプトを停止するボタンを設定します。

        通常、中央のボタンは実行中のスクリプトを停止するために使用されます。 
        この仕様を変更または無効にして、ボタンを他の目的に使用することができます。

        Arguments:
            button (Button): :attr:`Button.CENTER <pybricks.parameters.Button.CENTER>`などのボタン、またはボタンのタプルを指定します。
            ``None``を選択すると、ボタンを無効にします。
            無効にした場合は中央のボタンを3秒間長押しして、Hubの電源をオフにしてプログラムを停止することができます。
        """

    def shutdown(self) -> None:
        """shutdown()

        Stops your program and shuts the hub down."""

    def reset_reason(self) -> int:
        """reset_reason() -> int

        Finds out how and why the hub (re)booted. This can be useful to
        diagnose some problems.

        Returns:
            * ``0`` if the hub was previously powered off
              normally.
            * ``1`` if the hub rebooted automatically, like
              after a firmware update.
            * ``2`` if the hub previously
              crashed due to a watchdog timeout, which indicates a firmware
              issue.
        """

    def name(self) -> str:
        """name() -> str

        Gets the hub name. This is the name you see when connecting
        via Bluetooth.

        Returns:
            The hub name.
        """

    @overload
    def storage(self, offset: int, *, read: int) -> bytes: ...

    @overload
    def storage(self, offset: int, *, write: bytes) -> None: ...

    def storage(self, offset, read=None, write=None):
        """
        storage(offset, write=)
        storage(offset, read=) -> bytes

        Reads or writes binary data to persistent storage.

        This lets you store data that can be used the next time you run the
        program.

        The data will be saved to flash memory when you turn the hub off
        normally. It will not be saved if the batteries are removed *while* the
        hub is still running.

        Once saved, the data will remain available even after you remove the
        batteries.

        Args:
            offset (int): The offset from the start of the user storage memory, in bytes.
            read (int): The number of bytes to read. Omit this argument when writing.
            write (bytes): The bytes to write. Omit this argument when reading.

        Returns:
            The bytes read if reading, otherwise ``None``.

        Raises:
            ValueError:
                If you try to read or write data outside of the allowed range.
        """


class DCMotor:
    """Generic class to control simple motors without rotation sensors, such
    as train motors."""

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """

    def dc(self, duty: Number) -> None:
        """dc(duty)

        Rotates the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (Number, %): The duty cycle (-100.0 to 100).
        """

    def stop(self) -> None:
        """stop()

        Stops the motor and lets it spin freely.

        The motor gradually stops due to friction."""

    def brake(self) -> None:
        """brake()

        Passively brakes the motor.

        The motor stops due to friction, plus the voltage that
        is generated while the motor is still moving."""

    @overload
    def settings(self, max_voltage: Number) -> None: ...

    @overload
    def settings(self) -> Tuple[int]: ...

    def settings(self, *args):
        """
        settings(max_voltage)
        settings() -> Tuple[int]

        Configures motor settings. If no arguments are given,
        this returns the current values.

        Arguments:
            max_voltage (Number, mV):
                Maximum voltage applied to the motor during all motor commands.
        """


class Control:
    """Class to interact with PID controller and settings."""

    scale: int

    """
    Scaling factor between the controlled integer variable
    and the physical output. For example, for a single
    motor this is the number of encoder pulses per degree of rotation.
    """

    @overload
    def limits(
        self,
        speed: Optional[Number] = None,
        acceleration: Optional[Number] = None,
        torque: Optional[Number] = None,
    ) -> None: ...

    @overload
    def limits(self) -> Tuple[int, int, int]: ...

    def limits(self, *args):
        """
        limits(speed, acceleration, torque)
        limits() -> Tuple[int, int, int]

        Configures the maximum speed, acceleration, and torque.

        If no arguments are given, this will return the current values.

        The new ``acceleration`` and ``speed`` limit will become effective
        when you give a new motor command. Ongoing maneuvers are not affected.

        Arguments:
            speed (Number, deg/s or Number, mm/s):
                Maximum speed. All speed commands will be capped to this value.
            acceleration (Number, deg/s² or Number, mm/s²):
                Slope of the speed curve when accelerating or decelerating.
                Use a tuple to set acceleration and deceleration separately.
                If one value is given, it is used for both.
            torque (:ref:`torque`):
                Maximum feedback torque during control.
        """

    @overload
    def pid(
        self,
        kp: Optional[Number] = None,
        ki: Optional[Number] = None,
        kd: Optional[Number] = None,
        integral_deadzone: Optional[Number] = None,
        integral_rate: Optional[Number] = None,
    ) -> None: ...

    @overload
    def pid(self) -> Tuple[int, int, int, int, int]: ...

    def pid(self, *args):
        """pid(kp, ki, kd, integral_deadzone, integral_rate)
        pid() -> Tuple[int, int, int, int, int]

        Gets or sets the PID values for position and speed control.

        If no arguments are given, this will return the current values.

        Arguments:
            kp (int): Proportional position control
                constant. It is the feedback torque per degree of
                error: µNm/deg.
            ki (int): Integral position control constant. It is the feedback
                torque per accumulated degree of error: µNm/(deg s).
            kd (int): Derivative position (or proportional speed) control
                constant. It is the feedback torque per
                unit of speed: µNm/(deg/s).
            integral_deadzone (Number, deg or Number, mm): Zone around the
                target where the error integral does not accumulate errors.
            integral_rate (Number, deg/s or Number, mm/s): Maximum rate at
                which the error integral is allowed to grow.
        """

    @overload
    def target_tolerances(
        self, speed: Optional[Number] = None, position: Optional[Number] = None
    ) -> None: ...

    @overload
    def target_tolerances(self) -> Tuple[int, int]: ...

    def target_tolerances(self, *args):
        """target_tolerances(speed, position)
        target_tolerances() -> Tuple[int, int]

        Gets or sets the tolerances that say when a maneuver is done.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (Number, deg/s or Number, mm/s): Allowed deviation
                from zero speed before motion is considered complete.
            position (Number, deg or :ref:`distance`): Allowed
                deviation from the target before motion is considered
                complete.
        """

    @overload
    def stall_tolerances(
        self, speed: Optional[Number] = None, time: Optional[Number] = None
    ) -> None: ...

    @overload
    def stall_tolerances(self) -> Tuple[int, int]: ...

    def stall_tolerances(self, speed, time):
        """stall_tolerances(speed, time)
        stall_tolerances() -> Tuple[int, int]

        Gets or sets stalling tolerances.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (Number, deg/s or Number, mm/s): If the controller
                cannot reach this speed for some ``time`` even with maximum
                actuation, it is stalled.
            time (Number, ms): How long the controller has to be below this
                minimum ``speed`` before we say it is stalled.
        """


class Model:
    """Class to interact with motor state observer and settings."""

    def state(self) -> Tuple[float, float, float, bool]:
        """state() -> Tuple[float, float, float, bool]

        Gets the estimated angle, speed, current, and stall state of the motor,
        using a simulation model that mimics the real motor.
        These estimates are updated faster than the real measurements,
        which can be useful when building your own PID controllers.

        For most applications it is better to used the *measured*
        :meth:`angle <pybricks.pupdevices.Motor.angle>`,
        :meth:`speed <pybricks.pupdevices.Motor.speed>`,
        :meth:`load <pybricks.pupdevices.Motor.load>`, and
        :meth:`stall <pybricks.pupdevices.Motor.stalled>` state instead.

        Returns:
            Tuple with the estimated angle (deg), speed (deg/s), current (mA),
            and stall state (``True`` or ``False``).
        """

    @overload
    def settings(self, values: tuple) -> None: ...

    @overload
    def settings(self) -> tuple: ...

    def settings(self, speed, time):
        """settings(values)
        settings() -> Tuple

        Gets or sets model settings as a tuple of integers. If no arguments are
        given, this will return the current values. This method is mainly used
        to debug the motor model class. Changing these settings should not be
        needed in user programs.

        .. _model settings: https://docs.pybricks.com/projects/pbio/en/latest/struct__pbio__observer__settings__t.html

        Arguments:
            values (Tuple): Tuple with `model settings`_.
        """


class Motor(DCMotor):
    """Generic class to control motors with built-in rotation sensors."""

    control = Control()
    """The motors use PID control to accurately track the speed and
    angle targets that you specify. You can change its behavior through the
    ``control`` attribute of the motor. See :ref:`control` for an overview
    of available methods."""

    model = Model()
    """Model representing the observer that estimates the motor state."""

    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle.
            gears (list):
                List of gears linked to the motor. The gear connected
                to the motor comes first and the gear connected to the output
                comes last.

                For example: ``[12, 36]`` represents a gear train with a
                12-tooth gear connected to the motor and a 36-tooth gear
                connected to the output. Use a list of lists for multiple
                gear trains, such as ``[[12, 36], [20, 16, 40]]``.

                When you specify a gear train, all motor commands and settings
                are automatically adjusted to account for the resulting gear
                ratio. The motor direction remains unchanged by this.
            reset_angle (bool):
                Choose ``True`` to reset the rotation sensor value to the
                absolute marker angle (between -180 and 179).
                Choose ``False`` to keep the
                current value, so your program knows where it left off last
                time.
            profile (Number, deg): Precision profile. This is the approximate
                position tolerance in degrees that is acceptable in your
                application. A lower value gives more precise but more erratic
                movement; a higher value gives less precise but smoother
                movement. If no value is given, a suitable profile for this
                motor type will be selected automatically (about 11 degrees).
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Gets the rotation angle of the motor.

        Returns:
            Motor angle.
        """

    def speed(self, window: Number = 100) -> int:
        """speed(window=100) -> int: deg/s

        Gets the speed of the motor.

        The speed is measured as the change in the motor angle during the
        given time window. A short window makes the speed value more
        responsive to motor movement, but less steady. A long window makes the
        speed value less responsive, but more steady.

        Arguments:
            window (Number, ms): The time window used to determine the speed.

        Returns:
            Motor speed.

        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Checks if the motor is currently stalled.

        It is stalled when it cannot reach the target speed or position, even
        with the maximum actuation signal.

        Returns:
            ``True`` if the motor is stalled, ``False`` if not.
        """

    def load(self) -> int:
        """load() -> int: mNm

        Estimates the load that holds back the motor when it tries to move.

        Returns:
            The load torque.
        """

    def reset_angle(self, angle: Optional[Number]) -> None:
        """
        reset_angle(angle)

        Sets the accumulated rotation angle of the motor to a desired value.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
        """

    def hold(self) -> None:
        """hold()

        Stops the motor and actively holds it at its current angle."""

    def run(self, speed: Number) -> None:
        """run(speed)

        Runs the motor at a constant speed.

        The motor accelerates to the given speed and keeps running at this
        speed until you give a new command.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
        """

    def run_time(
        self, speed: Number, time: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """run_time(speed, time, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed for a given amount of time.

        The motor accelerates to the given speed, keeps running at this speed,
        and then decelerates. The total maneuver lasts for exactly the given
        amount of ``time``.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            time (Number, ms): Duration of the maneuver.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                with the rest of the program.
        """

    def run_angle(
        self,
        speed: Number,
        rotation_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed by a given angle.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            rotation_angle (Number, deg): Angle by which the motor should
                rotate.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                with the rest of the program.
        """

    def run_target(
        self,
        speed: Number,
        target_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_target(speed, target_angle, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed towards a given target angle.

        The direction of rotation is automatically selected based on the target
        angle. It does not matter if ``speed`` is positive or negative.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            target_angle (Number, deg): Angle that the motor should rotate to.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the motor to reach the target
                before continuing with the rest of the program.
        """

    def run_until_stalled(
        self,
        speed: Number,
        then: Stop = Stop.COAST,
        duty_limit: Optional[Number] = None,
    ) -> MaybeAwaitableInt:
        """
        run_until_stalled(speed, then=Stop.COAST, duty_limit=None) -> int: deg

        Runs the motor at a constant speed until it stalls.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            then (Stop): What to do after coming to a standstill.
            duty_limit (Number, %): Duty cycle limit during this
                command. This is useful to avoid applying the full motor
                torque to a geared or lever mechanism. If it is ``None``, the
                duty limit won't be changed during this command.

        Returns:
            Angle at which the motor becomes stalled.
        """

    def done(self) -> bool:
        """done() -> bool

        Checks if an ongoing command or maneuver is done.

        Returns:
            ``True`` if the command is done, ``False`` if not.
        """

    def track_target(self, target_angle: Number) -> None:
        """track_target(target_angle)

        Tracks a target angle. This is similar to :meth:`.run_target`, but
        the usual smooth acceleration is skipped: it will move to the target
        angle as fast as possible. This method is useful if you want to
        continuously change the target angle.

        Arguments:
            target_angle (Number, deg): Target angle that the motor should
                rotate to.
        """

    def close(self) -> None:
        """close()

        Closes the motor object so you can call ``Motor`` again to initialize
        a new object.

        This allows advanced users to change properties such as gearing in the
        middle of the program, which can be useful for removeable attachments.
        """


class Speaker:
    """Plays beeps and sounds using a speaker."""

    @overload
    def volume(self, volume: Number) -> None: ...

    @overload
    def volume(self) -> int: ...

    def volume(self, *args):
        """volume(volume)
        volume() -> int: %

        Gets or sets the speaker volume.

        If no volume is given, this method returns the current volume.

        Arguments:
            volume (Number, %): Volume of the speaker in the 0-100 range.
        """

    def beep(self, frequency: Number = 500, duration: Number = 100) -> MaybeAwaitable:
        """beep(frequency=500, duration=100)

        Play a beep/tone.

        Arguments:
            frequency (Number, Hz):
                Frequency of the beep in the 64-24000 Hz range.
            duration (Number, ms):
                Duration of the beep. If the duration is less
                than 0, then the method returns immediately and the frequency
                play continues to play indefinitely.
        """

    def play_notes(self, notes: Iterable[str], tempo: Number = 120) -> MaybeAwaitable:
        """play_notes(notes, tempo=120)

        Plays a sequence of musical notes. For example:
        ``["C4/4", "C4/4", "G4/4", "G4/4"]``.

        Each note is a string with the following format:

            - The first character is the name of the note, ``A`` to ``G``
              or ``R`` for a rest.
            - Note names can also include an accidental ``#`` (sharp) or
              ``b`` (flat). ``B#``/``Cb`` and ``E#``/``Fb`` are not
              allowed.
            - The note name is followed by the octave number ``2``
              to ``8``. For example ``C4`` is middle C. The octave changes
              to the next number at the note C, for example, ``B3`` is the
              note below middle C (``C4``).
            - The octave is followed by ``/`` and a number that indicates
              the size of the note. For example ``/4`` is a quarter note,
              ``/8`` is an eighth note and so on.
            - This can optionally followed by a ``.`` to make a dotted
              note. Dotted notes are 1-1/2 times as long as notes without a
              dot.
            - The note can optionally end with a ``_`` which is a tie or a
              slur. This causes there to be no pause between this note and
              the next note.

        Arguments:
            notes (iter):
                A sequence of notes to be played.
            tempo (int):
                Beats per minute. A quarter note is one beat.
        """


class ColorLight:
    """Control a multi-color light."""

    def on(self, color: Color) -> None:
        """on(color)

        指定した色でライトを点灯します。

        Arguments:
            color (Color): ライトの色
        """

    def off(self) -> None:
        """off()

        ライトを消します。
        """

    def blink(self, color: Color, durations: Collection[Number]) -> None:
        """blink(color, durations)

        ライトを一定時間、指定した色で点滅させます。

        ライトはプログラム実行中、バックグラウンドでずっと点滅し続けます。

        このメソッドでは、簡単で便利な点滅パターンを作成できます。
        より複雑なパターンを作成するには、代わりに ``animate()`` を使用してください。

        Arguments:
            color (Color): ライトの色
            durations (list): ``[on_1, off_1, on_2, off_2, ...]``といった形式で時間値を指定します。
        """

    def animate(self, colors: Collection[Color], interval: Number) -> None:
        """animate(colors, interval)

        指定された間隔で1つずつ表示される色のシーケンスでライトをアニメーション化します。

        アニメーションはバックグラウンドで実行されます。 
        アニメーションが完了すると最初に戻り、繰り返されます。

        Arguments:
            colors (list): :class:`Color <.parameters.Color>`のシーケンス
            interval (Number, ms): 色の更新間隔
        """


class ExternalColorLight:
    """Control a multi-color light."""

    def on(self, color: Color) -> MaybeAwaitable:
        """on(color)

        Turns on the light at the specified color.

        Arguments:
            color (Color): Color of the light.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Turns off the light.
        """


class LightArray3:
    """Control an array of three single-color lights."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Turns on the lights at the specified brightness.

        Arguments:
            brightness (Number or tuple, %):
                Use a single value to set the brightness of all lights at the
                same time. Use a tuple of three values to set the brightness
                of each light individually.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Turns off all the lights.
        """


class LightArray4(LightArray3):
    """Control an array of four single-color lights."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Turns on the lights at the specified brightness.

        Arguments:
            brightness (Number or tuple, %):
                Use a single value to set the brightness of all lights at the
                same time. Use a tuple of four values to set the brightness
                of each light individually. The order of the lights is shown
                in the image above.
        """


class LightMatrix:
    """Control a rectangular grid of single-color lights."""

    def __init__(self, rows: int, columns: int):
        """LightMatrix(rows, columns)

        Initializes the light matrix display.

        Arguments:
            rows (int): Number of rows in the grid
            columns (int): Number of columns in the grid
        """

    def orientation(self, up: Side) -> None:
        """orientation(up)

        ライトマトリクスの表示を回転させます。

        実行後、新たに表示されるピクセルだけが影響を受けます。
        既存の表示内容は変化しません。

        Arguments:
            top (Side): ライトマトリクスのどの面を「上」にするか。
            ``Side.TOP``、``Side.LEFT``、``Side.RIGHT``、``Side.BOTTOM``から選びます。
        """

    def icon(self, icon: Matrix) -> None:
        """icon(icon)

        :ref:`brightness`の輝度でアイコンを表示します。

        Arguments:
            icon (Matrix): 強度のマトリクス（:ref:`brightness`）。2Dリストも受け付けます。
        """

    def animate(self, matrices: Collection[Matrix], interval: Number) -> None:
        """animate(matrices, interval)

        画像のリストを使って作られたアニメーションを表示します。

        各画像は上記と同じフォーマットである。
        それぞれの画像は与えられた間隔だけ表示される。
        このアニメーションは、あなたのプログラムの残りの部分が動き続けている間、永遠に繰り返される。

        Arguments:
            matrices (iter): :class:`Matrix <pybricks.tools.Matrix>`のシーケンス。
            interval (Number, ms): リスト内の各画像を表示する時間。
        """

    def pixel(self, row: Number, column: Number, brightness: Number = 100) -> None:
        """pixel(row, column, brightness=100)

        指定された明るさで1つのピクセルをオンにします。

        Arguments:
            row (Number): 垂直方向の座標。上から0で始まります。
            column (Number): 水平方向の座標。左から0で始まります。
            brightness (Number :ref:`brightness`): ピクセルの明るさ。
        """

    def off(self) -> None:
        """off()

        すべてのピクセルをオフにします。"""

    def number(self, number: Number) -> None:
        """number(number)

        -99から99の範囲の数字を表示する。

        マイナス記号（``-``）はディスプレイの中央に点で表示されます。
        99以上の数字は``>``、99未満の数字は``<```で表示されます。

        Arguments:
            number (int): 表示する数字。
        """

    def char(self, char: str) -> None:
        """char(char)

        ライトマトリクスに文字または記号を表示します。
        任意の文字（``a``から``z``、``A``から``Z``）または以下の記号を表示できます。

        ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``

        Arguments:
            character (str): 表示する文字または記号。
        """

    def text(self, text: str, on: Number = 500, off: Number = 50) -> None:
        """text(text, on=500, off=50)

        テキストを1文字ずつ表示します。 
        最後の文字が表示された後にすべてのライトが消灯します。

        Arguments:
            text (str): 表示するテキスト。
            on (Number, ms): 1文字が表示される時間。
            off (Number, ms): 文字と文字の間の表示が消えている時間。
        """


class Keypad:
    """Get status of buttons on a keypad layout."""

    def __init__(self, active_buttons): ...

    def pressed(self) -> Set[Button]:
        """pressed() -> Set[Button]

        現在どのボタンが押されているか取得する。

        Returns:
            押されたボタンのセット。
        """


class Battery:
    """Get the status of a battery."""

    def voltage(self) -> int:
        """voltage() -> int: mV

        Gets the voltage of the battery.

        Returns:
            Battery voltage.
        """

    def current(self) -> int:
        """current() -> int: mA

        Gets the current supplied by the battery.

        Returns:
            Battery current.
        """


class Charger:
    """Get the status of a battery charger."""

    def connected(self) -> bool:
        """connected() -> bool

        Checks whether a charger is connected via USB.

        Returns:
            ``True`` if a charger is connected, ``False`` if not.
        """

    def status(self) -> int:
        """status() -> int

        Gets the status of the battery charger, represented by one of the
        following values. This corresponds to the battery light indicator
        right next to the USB port.

            0. Not charging (light is off).
            1. Charging (light is red).
            2. Charging is complete (light is green).
            3. There is a problem with the charger (light is yellow).

        Returns:
            Status value.
        """

    def current(self) -> int:
        """current() -> int: mA

        Gets the charging current.

        Returns:
            Charging current.
        """


class SimpleAccelerometer:
    """Get measurements from an accelerometer."""

    def acceleration(self) -> Tuple[int, int, int]:
        """acceleration() -> Tuple[int, int, int]: mm/s²

        Gets the acceleration of the device.

        Returns:
            Acceleration along all three axes.
        """

    def up(self) -> Side:
        """up() -> Side

        Hubのどの面が上を向いているかを取得します。

        Returns:
            ``Side.TOP``、``Side.BOTTOM``、``Side.LEFT``、``Side.RIGHT``、
            ``Side.FRONT``、``Side.BACK``のいずれか。
        """

    def tilt(self) -> Tuple[int, int]:
        """tilt() -> Tuple[int, int]

        ピッチ角とロール角を取得する。 これは、:ref:`ユーザーが指定した方向 <robotframe>`からの相対値です。

        回転の順序は、ピッチ-ターン-ロールです。これはロボットのY軸に沿って正回転し、次にX軸に沿って正回転することに相当します。

        Returns:
            ピッチ角とロール角を度単位で表したタプル。
        """


class Accelerometer(SimpleAccelerometer):
    """Get measurements from an accelerometer."""

    @overload
    def acceleration(self, axis: Axis) -> float: ...

    @overload
    def acceleration(self) -> Matrix: ...

    def acceleration(self, *args):
        """
        acceleration(axis) -> float: mm/s²
        acceleration() -> vector: mm/s²


        :ref:`ロボットフレーム <robotframe>`における、指定された軸に沿ったデバイスの加速度を取得します。

        Arguments:
            axis (Axis): 加速度を測定する軸。

        Returns:
            指定された軸に沿った加速度。 軸を指定しない場合は、すべての軸に沿った加速度のベクトルを返す。
        """


class IMU(Accelerometer):
    def ready(self) -> bool:
        """ready() -> bool

        IMUが使用可能かどうかを確認します。

        これは、ロボットが数秒間静止しているときに``True``になり、デバイスを再較正することができます。
        ハブが起動したばかりであったり、10分以上較正の機会がなかったりすると```False```になります。

        Returns:
            使用可能であれば``True``、そうでなければ``False``。
        """

    def stationary(self) -> bool:
        """stationary() -> bool

        現在のハブが静止しているかどうかを確認します。

        Returns:
            少なくとも1秒間静止していれば``True``、動いていれば``False``。
        """

    @overload
    def settings(
        self,
        angular_velocity_threshold: float = None,
        acceleration_threshold: float = None,
    ) -> None: ...

    @overload
    def settings(self) -> Tuple[float, float]: ...

    def settings(self, *args):
        """
        settings(angular_velocity_threshold, acceleration_threshold)
        settings() -> Tuple[float, float]

        IMUの設定を行います。 引数が与えられていない場合は、現在の値を返します。

        角速度しきい値（``angular_velocity_threshold``）と加速度しきい値（``acceleration_threshold``）は、
        Hubが静止しているとみなされるタイミングを定義します。 
        すべての測定値がこれらのしきい値を1秒間下回った場合、IMUは再キャリブレーションを行います。

        周囲の振動が大きい騒がしい部屋（競技会場など）では、ロボットにキャリブレーションの機会を与えるため、
        しきい値を少し大きくすることをお勧めします。設定が期待通りに機能していることを確認するには、``stationary()``メソッドが、
        ロボットが動いている場合は``False``を、少なくとも1秒間静止している場合は``True``を返すことをテストしてください。

        Arguments:
            angular_velocity_threshold (Number, deg/s): 角速度のしきい値。 デフォルト値は1.5deg/s。
            acceleration_threshold (Number, mm/s²): 角速度のしきい値。 デフォルト値は250 mm/s²。
        """

    def heading(self) -> float:
        """heading() -> float: deg

        ロボットの水平面での角度(方位角)を取得します。 正の値は時計回りを意味します。

        プログラム開始時の値は0です。この値はロボットが180度以上回転しても増え続けます。-180度まで折り返すことはありません。


        .. note:: このメソッドはロボットが平らな場所にいる間だけ記録しています。
                  つまり、ロボットをテーブルから持ち上げると、角度は正しくなくなってしまいます。
                  この問題を解決するには、``reset_heading``を呼び出すことで、ロボットを置いた後に既知の値にリセットすることができます。
                  例えば、ロボットを競技テーブルの側面に合わせ、新しい出発点としてリセットすることができます。

        Returns:
            開始方位に対するロボットの方位角。

        """

    def reset_heading(self, angle: Number) -> None:
        """reset_heading(angle)

        ロボットの方位角をリセットします。

        Arguments:
            angle (Number, deg): リセットする値。
        """

    @overload
    def angular_velocity(self, axis: Axis) -> float: ...

    @overload
    def angular_velocity(self) -> Matrix: ...

    def angular_velocity(self, *args):
        """
        angular_velocity(axis) -> float: deg/s
        angular_velocity() -> vector: deg/s

        :ref:`ロボットフレーム <robotframe>`における、指定された軸に沿ったデバイスの角速度を取得します。

        Arguments:
            axis (Axis): 角速度を測定する軸。
        Returns:
            指定された軸に沿った角速度。 軸を指定しない場合は、すべての軸に沿った加速度のベクトルを返す。
        """

    def rotation(self, axis: Axis) -> float:
        """
        rotation(axis) -> float: deg

        :ref:`ロボットフレーム <robotframe>`における、指定された軸に沿ったデバイスの回転を取得します。

        この値は、ロボットが要求された軸に沿ってのみ回転する場合に便利です。
        一般的な3次元モーションの場合は、代わりに``orientation()``メソッドを使用します。

        このクラスが初期化されると、値は``0``からカウントを開始します。

        Arguments:
            axis (Axis): 回転を測定する軸。
        Returns:
            回転した角度。
        """

    def orientation(self) -> Matrix:
        """
        orientation() -> Matrix

        :ref:`ロボットフレーム <robotframe>`における、ロボットの3次元姿勢を取得する。

        ロボットの``X``軸、``Y``軸、``Z``軸を表す回転行列を返します。

        .. note:: この方法はまだ実装されていません。

        Returns:
            ロボットの3次元姿勢を表す回転行列。
        """


class CommonColorSensor:
    """Generic color sensor that supports Pybricks color calibration."""

    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def color(self) -> MaybeAwaitableColor:
        """color() -> Color

        Scans the color of a surface.

        You choose which colors are detected using the
        ``detectable_colors()`` method. By default, it detects
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, or ``Color.NONE``.

        Returns:
            Detected color.
        """

    def hsv(self) -> MaybeAwaitableColor:
        """hsv() -> Color

        Scans the color of a surface.

        This method is similar to ``color()``, but it gives the full range
        of hue, saturation and brightness values, instead of rounding it to the
        nearest detectable color.

        Returns:
            Measured color. The color is described by a hue (0--359), a
            saturation (0--100), and a brightness value (0--100).
        """

    def ambient(self) -> MaybeAwaitableInt:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark)
            to 100% (bright).
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Measures how much a surface reflects the light emitted by the
        sensor.

        Returns:
            Measured reflection, ranging from 0% (no reflection) to
            100% (high reflection).
        """

    @overload
    def detectable_colors(self, colors: Collection[Color]) -> None: ...

    @overload
    def detectable_colors(self) -> Collection[Color]: ...

    def detectable_colors(self, *args):
        """
        detectable_colors(colors)
        detectable_colors() -> Collection[Color]

        Configures which colors the ``color()`` method should detect.

        Specify only colors that you wish to detect in your application.
        This way, the full-color measurements are rounded to the nearest
        desired color, and other colors are ignored. This improves reliability.

        If you give no arguments, the currently chosen colors will be returned.

        When coding with blocks, this is configured in the sensor setup block.

        Arguments:
            colors (list or tuple): List of :class:`Color <.parameters.Color>`
                objects: the colors that you want to detect. You can pick
                standard colors such as ``Color.MAGENTA``, or provide your
                own colors like ``Color(h=348, s=96, v=40)`` for even
                better results. You measure your own colors with the
                ``hsv()`` method.
        """


class AmbientColorSensor(CommonColorSensor):
    """Like CommonColorSensor, but also detects ambient colors when the sensor
    light is turned off"""

    def color(self, surface: bool = True) -> MaybeAwaitableColor:
        """color(surface=True) -> Color

        Scans the color of a surface or an external light source.

        You choose which colors are detected using the
        ``detectable_colors()`` method. By default, it detects
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, or ``Color.NONE``.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        Returns:
            Detected color.`
        """

    def hsv(self, surface: bool = True) -> MaybeAwaitableColor:
        """hsv(surface=True) -> Color

        Scans the color of a surface or an external light source.

        This method is similar to ``color()``, but it gives the full range
        of hue, saturation and brightness values, instead of rounding it to the
        nearest detectable color.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        Returns:
            Measured color. The color is described by a hue (0--359), a
            saturation (0--100), and a brightness value (0--100).
        """


class BLE:
    """
    Bluetooth Low Energy.

    .. versionadded:: 3.3
    """

    def broadcast(self, data: Union[bool, int, float, str, bytes]) -> None:
        """broadcast(data)

        Starts broadcasting the given data on
        the ``broadcast_channel`` you selected when initializing the hub.

        Data may be of type ``int``, ``float``, ``str``, ``bytes``,
        ``True``, or ``False``, or a list thereof.

        Choose ``None`` to stop broadcasting. This helps improve performance
        when you don't need the broadcast feature, especially when observing
        at the same time.

        The total data size is quite limited (26 bytes). ``True`` and
        ``False`` take 1 byte each. ``float`` takes 5 bytes. ``int`` takes 2 to
        5 bytes depending on how big the number is. ``str`` and ``bytes`` take
        the number of bytes in the object plus one extra byte.

        When multitasking, only one task can broadcast at a time. To broadcast
        information from multiple tasks (or block stacks), you could use a
        dedicated separate task that broadcast new values when one or more
        variables change.

        Args:
            data: The value or values to be broadcast.

        .. versionadded:: 3.3
        """

    def observe(
        self, channel: int
    ) -> Optional[Tuple[Union[bool, int, float, str, bytes], ...]]:
        """observe(channel) -> bool | int | float | str | bytes | tuple | None

        Retrieves the last observed data for a given channel.

        Receiving data is more reliable when the hub is not connected
        to a computer or other devices at the same time.

        Args:
            channel (int): The channel to observe (0 to 255).

        Returns:
            The received data in the same format as it was sent, or ``None``
            if no recent data is available.

        .. versionadded:: 3.3
        """

    def signal_strength(self, channel: int) -> int:
        """signal_strength(channel) -> int: dBm

        Gets the average signal strength in dBm for the given channel.

        This indicates how near the broadcasting device is. Nearby devices
        may have a signal strength around -40 dBm, while far away devices
        might have a signal strength around -70 dBm.

        Args:
            channel (int): The channel number (0 to 255).

        Returns:
            The signal strength or ``-128`` if there is no recent observed data.

        .. versionadded:: 3.3
        """

    def version(self) -> str:
        """version() -> str

        Gets the firmware version from the Bluetooth chip.

        .. versionadded:: 3.3
        """
