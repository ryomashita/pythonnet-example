import pythonnet
import sys
import clr

# load .NET runtime (if use .Net Framework, not have to call this)
# pythonnet.load("netfx")
print(pythonnet.get_runtime_info())

# Before import the DLL assembly, have to build C# Project first
# `dotnet publish -c Release .\SampleNetLibForPythonNet\ -o .\release\`

# append the path of DLL to sys.path
sys.path.append("release")
# Import the DLL assembly (don't append `.dll` to the name)
reference = clr.AddReference("SampleNetLibForPythonNet")
# use `from <.Net namespace> import <.Net class>` to import
from CalcTestNS import calculate  # type: ignore # noqa: E402


def call_dll():
    calculate_obj = calculate()
    print(calculate_obj.Add(1, 2))  # -> 3
    print(calculate_obj.Sub(*[1, 2]))  # -> -1


# run following command to run this script with uv
# `uv run call_dll.py`

if __name__ == "__main__":
    call_dll()
