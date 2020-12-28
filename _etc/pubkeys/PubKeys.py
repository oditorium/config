# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Public Keys

# ## Preparation

from hashlib import md5 as hsh
from base64 import b64encode as encode
from collections import namedtuple

key_t = namedtuple("key_t", "device, account, date, keyid, keysig, key")


# +
def ksig(keyv):
    "calculate key signature"
    return encode(hsh(keyv.encode()).digest()).decode()[:4]

def process(row):
    "returns some easy to parse signature"
    key = row[-1]
    _, keyv, keyid = key.split(" ")
    keysig = ksig(keyv)
    result = row[:-1]+(keyid, keysig, f"{key}/{keysig}")
    #return result
    return key_t(*result)


# -

# ## Data

data = []

# ### MacBook Air 2020

data += [("MBA2020", "skl", "1-Sep-2020", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCeswbbVGYYy1nMAd9X2OAtDH7VUjJffDYTrRh5YUkiAHlJY7CVpZ9cHHDf8JzJj1I5DDE9OHHE5ZB5EkMjqPPeOkgseZkexMNjyDxZSTv9+4/JdBgWk7s5wNGtWid3yikdUg9pdRRUdyATjvNphLunS1nR9TS4wfBsL4Hqhl5IOn/TOwPxMZ2Bn37wfXsLPKtQxaJo7lY3m9ZX8b+38qF7bOGrYDLWzUcH8VwgizNT0camRvUcgAaMYSI4+Mz8HtakQtCwXE+iMgAndZNx0UNW9uzL7yrc2fHDMy/7PJXQx2V2ENDPZx494wP+DNG0l6zamDSZTLToaktM49ut3r9anCqwru3Fp63G0amJ1Gc4x70yWHTE/vPUPzCOB2Y/dOb5eY6u1CKBMGOSvBy19hWQmQjZtBmgEeKjpbalGcFCEeE7K8SvXvdUPKGJUrfc5ke3oDpXW9Ei353lAgOz2VPfigby20HVAlTu3r200L4q39PO2/1QecFZFzt/azhLlpU= skl@MBA2020v2")]

# ### iPad Pro 2019

data += [("iPadPro2019", "Blink", "1-Jan-2019", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6Vh+Oag8gVlN91mxCA2yipKXPtprV5LK/v6XKVCGg56TwwLyv+Mg72xXq9TAxJJZK2saVA/1dljKgmQu+9PRPjI4/lKZSH5UMVOCm7X5rL1Vrycfp49oAJYr8RC5a2T7+EGEiTxjuwmjQcCbLCvO8v3ZFDd4cFU2E4CGXwuAsU9Xhos8nKGx/uX6n96AMXRHy/dBAttdw+PRUNR7IFSTnJr89Efn8Ys9AfzbBzrhkEyKd9DFiz7TfzRAnzqXqAIKTRypYOUhvqRGTIOH3VNCEMaj0Pu83xN+n8mScjGz3BDgky3q/cA6mUU+9bI8GT1PaTp6XhLbwJd1udrD0TcQj Blink@iPadPro2019")]

data += [("iPadPro2019", "WorkingCopy", "1-Jan-2019", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCngwf+5Nvaf5ZWJuy7605DpVnq77FP/zlts3UJ10M7EEcvw7r24g5KGpliL6za0VW2sn9nF9M6Mvbhfb3VKQCwuCAyw96ZxSppj4yKCV4XimNXsT18mtuo6U8NzM8FQ3xNrp/xqPiwofSFAGiLgOhygyZvqEyR7+6KiMcTRJPhRZZ7I3yzTKCMYCoI8U8s1WcOHC6WJAp1iz1dBNeDHyO9XsmVU1ULGuTRIgvE7flpNYQoWwfO7va6qxBZynl0zW4SwgOImNPLFGSVoQaY1iBLgjJ19nrkeVquxfIMqp5V58HXFk0fk9AHTsUj/+mxBf950pCNSBU7SrMIjWkqbim9 WorkingCopy@iPadPro2019")]

data += [("iPadPro2019", "Termius", "1-Jan-2019", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDc2nwJorUUjLirj/ddqZ2Zx9ArP4ofmgUXgCOE75+i2mzxFzLVWJkn/s7rsXfgADBzqZ1l5ibO6wuRy1eGSBu0KngQZ2DG4kWccfUImdGQSYoHrQmSyN6HIT3tkxp8bCcPOGfBylyvsROb2jT5KHCmvLZ3JI6YerYup/kDinv71BlG9UHqiXRGJsJh7kymncK/snpHifbViJ8aTS4y3wQrhCuARUI9VrfPNWhkoioYyBfbz0G4JjU6gwFL+ldMb1j+aKTjY5s9CRCQkGkOl8+X38icBzM3O2dS6T4ZoQFzXJPKXXn1zWeLePCjQgtOfaUaWyqV6nMYPufrFCgFarAn Termius@iPadPro2019")]


# ### iPhone Red 2018

data += [("iPhoneRed2018", "Blink", "1-Jan-2018", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8YGQ0+86MR8ppXAUMbzv5darGSYLu/Bomyy6DwZN9eyjX7dRtch2xevUnI9xXXdS6RA/JhvvM9GxhorODQt4KHlRbuDU2Ei6xuGQftEgeP96+zSV7Y39dCRgf2vG1TDbX4LjdTHZ5enS9w51Dhy3ZZzCuRzODY5oRST6ZIM62F9myAL26yKcbebqrmStur3CnoVl39Aq7fMjT9T/ADdBSAFVskNIBaCS2Cchct2TcaO2SM9ElHQmcHt4um5PzmGKmG0hPiOzKnz38vdokX/YxDbivtcMtjcPlkMlXdxiAoRxUI9ll15prN2njrkMae4BLOL8EUqbubIRVv0LEOOmpgX89dgN4KWXAoYBDcCxiiH9hXxLY6Hhw/PKMqTzL5uWQYXppjQD9bZnf38s4I0blI09u3RTHykF3bxUbZgY26i/PSkaJFFtHWkvbGEB7AYWQabE1jvLMu6R1fxfUtHu90jjbv44k15JkKiy/rNyANUgWcl2arDW7DJoJd6gG+vvurEd25t/ZthGStE0Ng8NpLd0PFP9U59oYC/MYlS92p3I626m/Pz4rUWku4Rg5v9FnOLeNVP/oFxqxKi43/vdSQTl2fFa8jHxruHf9b1maaJ7qFGHiCH9zVOdgC8yktAk/24fy5a34qfmgEKBhf8wm6mywutp3OnSn5W/N6/SSJQ== Blink@iPhoneRed2018")]

data += [("iPhoneRed2018", "WorkingCopy", "1-Jan-2018", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDanM9xbPwwlq8fWwoPFIEg2oqJgWFf8JpRsGZiMBWf5/UKGMtLnVk9aHEIMuZIz9L7b6AWTeLC9qWBadp66mI/2QV3wAI+OFa/PWw5cGArakuNWcGzgHsDPrf0k17jTlomTrn0u+RTTC5zIzLvCGJAVoWJXqqZEnxFak/s7yYkWiEELpcfgQsN3+pngkPkxQ0VMkQ9S0rlFVnEu5gvEiSqaGcisDl7htKnqaY3l5j6pyadhIYviVKFxtmNUCDLr+0a31p6fgziLCwbP1aVX4XtS/Mw9oHtT8jPsM/1NlQuCBQ7JvWTJ9LEAXHY6VHDVCdsmwbX3d18fvTCw9B1Cdjh WorkingCopy@iPhoneRed2018")]

data += [("iPhoneRed2018", "Termius", "1-Jan-2018", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDoKtUqJmz7ttw1ebOWtcvAjxqtY1+d5VSbwcUAfUE3OmgOU0o1c/pVnPDM61/38/HZujkQMpzqjbnyg5w3I6Hy1yORwH2Fy854yK59QESGX2WAzd0GvOuBBKSKOdeE0SieVE4jx7LYhp23p96sWzzYxMaXfgfXLicORYwMCRgUM7i75xY89I4qn96757o+HQWssHpyRnJB2Tflj3jI/X4msSPdrl3Iz3EtHpkaj62T6tDRKFgn+y/pQYWh7imdvPkeCzxvW5SaKF/ffh/Xn+6NZYXFrTdyDLSk9J46surAnxfNcEkziUYtAALCLy/6ZUlbtxpFXc+PRCYaeMd+DXLD Termius@iPhoneRed2018")]

# ### iPad 2016

data += [("iPad2016", "Blink", "1-Jan-2016", None)]

data += [("iPad2016", "WorkingCopy", "1-Jan-2016", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBKNtM2qieAWlnw1YsJPUfMq5aX/3XZldRdiP2Tz6VpR6ZdMILAW+4SPffMg4FN/XTDylz+MpfvpNSCr+VNHSuf68lEXdPeXc7A5z2KPKtXGVzZxUtr7cnu94i6XAJrzSZKLgtNwXGyL8R8UA2HjlhTxrEJhGg2vqoobTghhqC3Gk4cxMbAWJlK+U7B0ydjUG6laGc4w7ugc2azjbd+L6ClKRKUbWysuy3GB05hb6A9rFjjPIi4cjA55gKjkjP/eqfn39+LfbyJkSA8xFehlIUsalP7E0ovogh3XDxL3rTg2V7Sh4lvpjhwHJgjiqtEi3DTx/L2rlT5/cd3MFOL0MJ WorkingCopy@iPad2016")]

data += [("iPad2016", "Termius", "1-Jan-2016", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1EMmLcZDZZTR6IAGShkijgXwzlrDcWK/Lbpu4Vqfm/k9/QiuWZEaGm6wxHHcu/eHk9VELqpYZ3hXSoVOSEpEZkO5ilcraN8207oERxY8vQVuACyAjHroI4320svTr5d4vmirTIk4LnsFj2C6Boh4kEaABbg04E0dBfaR7cJ8W4ojKjSXiz+XRPVLzi9/WllbLrPJbQ35wytCykuEiN1bY4/CgaLvzdA2aKskIr4QttHf4tLL3STQoM9d+q+rf7pPOGwTbXFNEhQ+Ygj4FPul9LWhfdNoB8qK8E4l96plDNh5tY7ST8A2pcsZ0TDvqAMTb4LeRz14skub83B3RI6jn Termius@iPad2016")]


# ## Execution

data_full = tuple(data)
keydata = tuple(process(r) for r in data if not r[-1] is None)
len(keydata), len(data_full)

keydata[1]

keys_bysig = {r.keysig: r for r in keydata}
keys_bysig_s = set(keys_bysig.keys())
keys_bysig_s

authorized_keys = "\n".join(r.key for r in keydata)
with open("authorized_keys", "w") as f: f.write(authorized_keys)
#print(authorized_keys)

# ## Analysis
#
# paste an authorized_keys file here to analyse it and compare it against known keys

server = "NA"
acct = "root"
home = "/root"
fullpath = f"{acct}@{server}:{home}/.ssh/authorized_keys"
fullpath 

# !rsync {fullpath} authorized_keys_far

authorized_keys_test = """
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCeswbbVGYYy1nMAd9X2OAtDH7VUjJffDYTrRh5YUkiAHlJY7CVpZ9cHHDf8JzJj1I5DDE9OHHE5ZB5EkMjqPPeOkgseZkexMNjyDxZSTv9+4/JdBgWk7s5wNGtWid3yikdUg9pdRRUdyATjvNphLunS1nR9TS4wfBsL4Hqhl5IOn/TOwPxMZ2Bn37wfXsLPKtQxaJo7lY3m9ZX8b+38qF7bOGrYDLWzUcH8VwgizNT0camRvUcgAaMYSI4+Mz8HtakQtCwXE+iMgAndZNx0UNW9uzL7yrc2fHDMy/7PJXQx2V2ENDPZx494wP+DNG0l6zamDSZTLToaktM49ut3r9anCqwru3Fp63G0amJ1Gc4x70yWHTE/vPUPzCOB2Y/dOb5eY6u1CKBMGOSvBy19hWQmQjZtBmgEeKjpbalGcFCEeE7K8SvXvdUPKGJUrfc5ke3oDpXW9Ei353lAgOz2VPfigby20HVAlTu3r200L4q39PO2/1QecFZFzt/azhLlpU= skl@MBA2020B
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDmfRuvkJaHM+Prg4otI7V7is+twpaEg10XXNXda+u56I0TE4hXrunN05EG/Tz0a2IndZw2bYzwxd/GM8YDHQi2Z4WAgN6POQW5aYP4YvLroJJxtxVwaGyxJaWK1kGcA7GrHcWK8BsjTeeDJghEHLq2DEhKrkn11lc7+05eSx5Mk9SXhhrtqQufE6bkzofMuNAw+CoZkI8LDbdmJIvXBG3P35AQmu5Zw+fJnpEepzJkzvqExBQw1It7ytGDD2eJ6ClovIhyYPqfXZZVCyAm9mKapxafdsNAmSUgJk1ACsIJv7VUMCa9h/+qM8BhPUz1pzWEjD2o/3P3cXPA0zvO2EVx skl@MBA.local
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA9S4Baa4drFo7fEWBvtk+kOzLGj9oP+EbWCWupA/TFdJiMfiQQp6d0aQDLVo8QxgrmWDyT3IEGGSuYWQuDZ02U5qw7a45AKsXt4BN7Xkd7RaTOvC+ogQFmjBmB90L7v3N+Jc2o/SzybAG80hXN5P6AYYTEZ9QjIaUKdUVCD7rhYOymdgRICM+WeFeLZ8GXeIyqYMUoQ8uD24OBaHD2rp2Jwhx4LkQ1GKMkzxTQhOKxoDDviQU6QDlFLLzdONdrT/X3oUL+19YgkVZTfA8Af1TwH5g20+X2nK6DSHFk3bxvSUVFayk1WQ2X/3IyLgnZUuGRDXIknplUdLpImKmp03NcQ== skl@mbp
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWjU/ClgoTzRCnBHZBE7C7upbpHtSKUj4Yo/9Qm0fGCKQ06+m6t6bnjlTR4HIyaWGtvtRahwNatsDFpxQnE+kYa+2xGlb4g908OGktmds3A1jvm7oBDhC0or0RxsnIreCdeqU/vJznTPWfwmwfbj+ojKFuAkAx8deGtZZ59EAgRigZKxw3aOeZ5+YdENAe/gmdpZ6FXkXo8J8JXs/J+fCGaf/6K841zn/B6RjZGeWHlL+f8NPBluNH/4dLCtCIJmLgbEnfmoVTNGR0U0649RWNzV1bEKkuiZbv6FD+sNVU5nMRwRrPhnK4hD7i5uw4OeFFdcFbqL4jasMS1iHf4vA9 sam@MBA
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDmfRuvkJaHM+Prg4otI7V7is+twpaEg10XXNXda+u56I0TE4hXrunN05EG/Tz0a2IndZw2bYzwxd/GM8YDHQi2Z4WAgN6POQW5aYP4YvLroJJxtxVwaGyxJaWK1kGcA7GrHcWK8BsjTeeDJghEHLq2DEhKrkn11lc7+05eSx5Mk9SXhhrtqQufE6bkzofMuNAw+CoZkI8LDbdmJIvXBG3P35AQmu5Zw+fJnpEepzJkzvqExBQw1It7ytGDD2eJ6ClovIhyYPqfXZZVCyAm9mKapxafdsNAmSUgJk1ACsIJv7VUMCa9h/+qM8BhPUz1pzWEjD2o/3P3cXPA0zvO2EVx skl@MBA.local
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDc2nwJorUUjLirj/ddqZ2Zx9ArP4ofmgUXgCOE75+i2mzxFzLVWJkn/s7rsXfgADBzqZ1l5ibO6wuRy1eGSBu0KngQZ2DG4kWccfUImdGQSYoHrQmSyN6HIT3tkxp8bCcPOGfBylyvsROb2jT5KHCmvLZ3JI6YerYup/kDinv71BlG9UHqiXRGJsJh7kymncK/snpHifbViJ8aTS4y3wQrhCuARUI9VrfPNWhkoioYyBfbz0G4JjU6gwFL+ldMb1j+aKTjY5s9CRCQkGkOl8+X38icBzM3O2dS6T4ZoQFzXJPKXXn1zWeLePCjQgtOfaUaWyqV6nMYPufrFCgFarAn Termius@iPadPro2
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1EMmLcZDZZTR6IAGShkijgXwzlrDcWK/Lbpu4Vqfm/k9/QiuWZEaGm6wxHHcu/eHk9VELqpYZ3hXSoVOSEpEZkO5ilcraN8207oERxY8vQVuACyAjHroI4320svTr5d4vmirTIk4LnsFj2C6Boh4kEaABbg04E0dBfaR7cJ8W4ojKjSXiz+XRPVLzi9/WllbLrPJbQ35wytCykuEiN1bY4/CgaLvzdA2aKskIr4QttHf4tLL3STQoM9d+q+rf7pPOGwTbXFNEhQ+Ygj4FPul9LWhfdNoB8qK8E4l96plDNh5tY7ST8A2pcsZ0TDvqAMTb4LeRz14skub83B3RI6jn Termius@iPad
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDoKtUqJmz7ttw1ebOWtcvAjxqtY1+d5VSbwcUAfUE3OmgOU0o1c/pVnPDM61/38/HZujkQMpzqjbnyg5w3I6Hy1yORwH2Fy854yK59QESGX2WAzd0GvOuBBKSKOdeE0SieVE4jx7LYhp23p96sWzzYxMaXfgfXLicORYwMCRgUM7i75xY89I4qn96757o+HQWssHpyRnJB2Tflj3jI/X4msSPdrl3Iz3EtHpkaj62T6tDRKFgn+y/pQYWh7imdvPkeCzxvW5SaKF/ffh/Xn+6NZYXFrTdyDLSk9J46surAnxfNcEkziUYtAALCLy/6ZUlbtxpFXc+PRCYaeMd+DXLD termius@iPhone8
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBKNtM2qieAWlnw1YsJPUfMq5aX/3XZldRdiP2Tz6VpR6ZdMILAW+4SPffMg4FN/XTDylz+MpfvpNSCr+VNHSuf68lEXdPeXc7A5z2KPKtXGVzZxUtr7cnu94i6XAJrzSZKLgtNwXGyL8R8UA2HjlhTxrEJhGg2vqoobTghhqC3Gk4cxMbAWJlK+U7B0ydjUG6laGc4w7ugc2azjbd+L6ClKRKUbWysuy3GB05hb6A9rFjjPIi4cjA55gKjkjP/eqfn39+LfbyJkSA8xFehlIUsalP7E0ovogh3XDxL3rTg2V7Sh4lvpjhwHJgjiqtEi3DTx/L2rlT5/cd3MFOL0MJ WorkingCopy@iPadBea
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCngwf+5Nvaf5ZWJuy7605DpVnq77FP/zlts3UJ10M7EEcvw7r24g5KGpliL6za0VW2sn9nF9M6Mvbhfb3VKQCwuCAyw96ZxSppj4yKCV4XimNXsT18mtuo6U8NzM8FQ3xNrp/xqPiwofSFAGiLgOhygyZvqEyR7+6KiMcTRJPhRZZ7I3yzTKCMYCoI8U8s1WcOHC6WJAp1iz1dBNeDHyO9XsmVU1ULGuTRIgvE7flpNYQoWwfO7va6qxBZynl0zW4SwgOImNPLFGSVoQaY1iBLgjJ19nrkeVquxfIMqp5V58HXFk0fk9AHTsUj/+mxBf950pCNSBU7SrMIjWkqbim9 WorkingCopy@iPadPro2
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDanM9xbPwwlq8fWwoPFIEg2oqJgWFf8JpRsGZiMBWf5/UKGMtLnVk9aHEIMuZIz9L7b6AWTeLC9qWBadp66mI/2QV3wAI+OFa/PWw5cGArakuNWcGzgHsDPrf0k17jTlomTrn0u+RTTC5zIzLvCGJAVoWJXqqZEnxFak/s7yYkWiEELpcfgQsN3+pngkPkxQ0VMkQ9S0rlFVnEu5gvEiSqaGcisDl7htKnqaY3l5j6pyadhIYviVKFxtmNUCDLr+0a31p6fgziLCwbP1aVX4XtS/Mw9oHtT8jPsM/1NlQuCBQ7JvWTJ9LEAXHY6VHDVCdsmwbX3d18fvTCw9B1Cdjh Workingcopy@iPhoneRed
"""

authorized_keys_test = authorized_keys_test.strip()

testkeys_bysig = {ksig(k.split()[1]): k for k in authorized_keys_test.split("\n")}
testkeys_bysig_s = set(testkeys_bysig.keys())
testkeys_bysig_s

known_keys_s = testkeys_bysig_s.intersection(keys_bysig_s)
known_keys = {s:r for s,r in keys_bysig.items() if s in known_keys_s}
known_keys.keys()
tuple((k.keyid, k.keysig) for k in known_keys.values())

unknown_keys_s = testkeys_bysig_s.difference(known_keys_s)
unknown_keys = {s:r for s,r in testkeys_bysig.items() if s in unknown_keys_s}
unknown_keys.keys()
tuple((k.split(" ")[-1], s) for s,k in unknown_keys.items())

missing_keys_s = keys_bysig_s.difference(known_keys_s)
missing_keys = {s:r for s,r in keys_bysig.items() if s in missing_keys_s}
missing_keys.keys()
tuple((k.keyid, k.keysig) for k in missing_keys.values())

missing_keys_ak = "\n".join(k.key for k in missing_keys.values())
print(missing_keys_ak)


