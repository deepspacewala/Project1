class AutomationError(Exception):
    """Base exception for automation errors"""
    pass

class TaskParsingError(AutomationError):
    """Raised when task parsing fails"""
    pass

class SecurityError(AutomationError):
    """Raised for security violations"""
    pass

class TaskExecutionError(AutomationError):
    """Raised when task execution fails"""
    pass 