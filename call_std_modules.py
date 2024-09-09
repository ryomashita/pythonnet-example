import clr


def main():
    # Using System namespace
    clr.AddReference("System.Drawing")
    from System.Drawing import Point  # type: ignore

    print(Point(1, 2))  # -> {X=1,Y=2}

    # Using Generics
    clr.AddReference("System.Collections")
    from System.Collections.Generic import Dictionary  # type: ignore
    from System import Console, String, Int32, UInt32, Type  # type: ignore

    print(Dictionary[String, String]())
    print(Dictionary[String, Int32]())
    print(Dictionary[String, Type]())
    print(Console.WriteLine.__overloads__[UInt32](42))  # select overload explicitly

    # Using Properties
    clr.AddReference("System")
    from System import Environment  # type: ignore

    name = Environment.MachineName
    Environment.ExitCode = 1
    print(name, Environment.ExitCode)

    # Using Indexers
    from System.Collections import Hashtable  # type: ignore

    table = Hashtable()
    table["key1"] = "value1"
    print(table["key1"])

    # Using Methods
    drives = Environment.GetLogicalDrives()
    print(drives)
    print(Environment.GetFolderPath.__doc__)  # view signature of GetFolderPath method
    # help(Environment.GetFolderPath)  # view help page of GetFolderPath method

    # Using out/ref parameters
    # `TryParse(string, out int) -> bool` returns (bool, int)
    success, value = Int32.TryParse("42")
    print(success, value)


# run following command to run this script with uv
# `uv run call_std_modules.py`

if __name__ == "__main__":
    main()
