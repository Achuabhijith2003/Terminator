class ReminderManager:
    def __init__(self):
        self.reminders = {}
        self.next_id = 1

    def add_reminder(self, time, message):
        reminder_id = self.next_id
        self.reminders[reminder_id] = {'time': time, 'message': message}
        self.next_id += 1
        return reminder_id

    def get_reminders(self):
        return self.reminders

    def remove_reminder(self, reminder_id):
        if reminder_id in self.reminders:
            del self.reminders[reminder_id]
            return True
        return False