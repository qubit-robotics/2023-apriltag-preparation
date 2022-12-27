import wpilib.drive
import commands2
import ctre

class Drive(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        self.drive_fLeft = ctre.WPI_VictorSPX(21)
        self.drive_rLeft = ctre.WPI_VictorSPX(23)
        self.drive_fRight = ctre.WPI_VictorSPX(22)
        self.drive_rRight = ctre.WPI_VictorSPX(24)

        self.drive_fLeft.setSafetyEnabled(0)
        self.drive_rLeft.setSafetyEnabled(0)
        self.drive_fRight.setSafetyEnabled(0)
        self.drive_rRight.setSafetyEnabled(0)

        self.drive = wpilib.drive.MecanumDrive(
            self.drive_fLeft,
            self.drive_rLeft,
            self.drive_fRight,
            self.drive_rRight
        )

    def driveMecanum(self, y_axis, x_axis, z_rotation):
        self.drive.driveCartesian(
            y_axis,
            x_axis,
            z_rotation
        )