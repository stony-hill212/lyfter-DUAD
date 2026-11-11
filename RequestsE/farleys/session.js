const SESSION_KEY= "currentUser";
const SESSION_DURATION= 5 * 60 * 1000;

function createSession(userId) {
    const session= {
        id: userId,
        loginTimestamp: Date.now()
    };
    localStorage.setItem(SESSION_KEY, JSON.stringify(session));
}
function getValidSession() {
    const storedSession= localStorage.getItem(SESSION_KEY);
    if (!storedSession) {return null;}
    try {
        const session= JSON.parse(storedSession);
        if (
            session.id== null ||
            typeof session.loginTimestamp!== "number"
        ) {
            localStorage.removeItem(SESSION_KEY);
            return null;
        }
        const elapsedTime= Date.now() - session.loginTimestamp;
        if (elapsedTime > SESSION_DURATION) {
            localStorage.removeItem(SESSION_KEY);
            sessionStorage.setItem(
                "sessionMessage",
                "Session expired, please login to your account"
            );
            return null;
        }
        return session;
    } catch (error) {
        localStorage.removeItem(SESSION_KEY);
        return null;
    }
}
function requireValidSession() {
    const session= getValidSession();
    if (!session) {
        window.location.replace("login.html");
        return null;
    }
    return session;
}