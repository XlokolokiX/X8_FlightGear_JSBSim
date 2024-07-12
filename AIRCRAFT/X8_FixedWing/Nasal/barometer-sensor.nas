print('Loading Barometer Sensor')

var barometer = {
    init: func {
        # Define and initialize internal properties
        props.globals.getNode("/sensors/barometer/time_us", 1, 0);
        props.globals.getNode("/sensors/barometer/presStatic_true_Pa", 1, 0.0);
        props.globals.getNode("/sensors/barometer/temp_true_C", 1, 0.0);
        props.globals.getNode("/sensors/barometer/presStatic_Pa", 1, 0.0);
        props.globals.getNode("/sensors/barometer/temp_C", 1, 0.0);

        # Set timers to update properties
        settimer(barometer.updateTimeUs, 0.1, 0.1);  # Update every 0.1 seconds
        settimer(barometer.updatePresStaticTruePa, 0.1, 0.1);
        settimer(barometer.updateTempTrueC, 0.1, 0.1);
        settimer(barometer.updateErrorModels, 0.1, 0.1);
    },

    updateTimeUs: func {
        var simTimeSec = getprop("/sim/time/elapsed-sec");
        setprop("/sensors/barometer/time_us", simTimeSec * 1000000.0);
        print("Updated /sensors/barometer/time_us to ", simTimeSec * 1000000.0);
    },

    updatePresStaticTruePa: func {
        var presPsf = getprop("/environment/atmosphere/pressure-psf");
        setprop("/sensors/barometer/presStatic_true_Pa", presPsf * 47.88026);
        print("Updated /sensors/barometer/presStatic_true_Pa to ", presPsf * 47.88026);
    },

    updateTempTrueC: func {
        var tempR = getprop("/environment/atmosphere/temperature-R");
        setprop("/sensors/barometer/temp_true_C", (tempR - 491.67) * 0.5555555555555556);
        print("Updated /sensors/barometer/temp_true_C to ", (tempR - 491.67) * 0.5555555555555556);
    },

    updateErrorModels: func {
        var presStaticTruePa = getprop("/sensors/barometer/presStatic_true_Pa");
        var tempTrueC = getprop("/sensors/barometer/temp_true_C");

        # Apply error models (for simplicity, this example does not add noise, drift, etc.)
        setprop("/sensors/barometer/presStatic_Pa", presStaticTruePa);
        setprop("/sensors/barometer/temp_C", tempTrueC);
        print("Updated /sensors/barometer/presStatic_Pa to ", presStaticTruePa);
        print("Updated /sensors/barometer/temp_C to ", tempTrueC);
    }
};

barometer.init();
