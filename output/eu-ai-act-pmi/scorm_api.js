// SCORM 1.2 API Wrapper
var scorm = {
    version: "1.2",
    handleError: function(errorCode) {
        console.error("SCORM Error " + errorCode);
    },
    get: function(parameter) {
        var API = this.getAPI();
        if (API) {
            var value = API.LMSGetValue(parameter);
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return value;
        }
        return "";
    },
    set: function(parameter, value) {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSSetValue(parameter, value);
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    initialize: function() {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSInitialize("");
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    commit: function() {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSCommit("");
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    finish: function() {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSFinish("");
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    getAPI: function() {
        var API = null;
        var findAPITries = 0;

        while ((API == null) && (findAPITries < 7)) {
            if (window.API != null) {
                API = window.API;
            } else if (window.parent != null && window.parent != window) {
                findAPITries++;
                window = window.parent;
            } else {
                findAPITries++;
            }
        }

        return API;
    }
};

function initializeSCORM() {
    scorm.initialize();
    scorm.set("cmi.core.lesson_status", "incomplete");
    scorm.set("cmi.core.session_time", "00:00:00");
    scorm.commit();
}

function completeSCORM() {
    scorm.set("cmi.core.lesson_status", "completed");
    scorm.set("cmi.core.score.raw", "100");
    scorm.commit();
    scorm.finish();
}
