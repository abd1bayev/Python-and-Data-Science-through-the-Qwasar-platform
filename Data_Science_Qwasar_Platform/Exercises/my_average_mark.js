function my_average_mark(param_1) {
    var a = 0;
    for (var i = 0; i < param_1.length; i++) {
        a += param_1[i]["integer"]
    }
    var avr = a/param_1.length
        if (param_1.length == 0) {
             return `0.0`
        }
        else {
            return avr.toFixed(1)
        }
    }