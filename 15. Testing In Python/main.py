# 1. Testing Introduction

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter number"
    except Exception as err:
        return err
