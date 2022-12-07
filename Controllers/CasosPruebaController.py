from Models.CasosPruebaModel import CasosPruebaModel
from Views.CasosPruebaView import CasosPruebaView


class CasosPruebaController:
    def __init__(self, root):
        self.model = CasosPruebaModel()

        self.view = CasosPruebaView(root)
        self.view.grid(row=0, column=0, padx=10, pady=10)
        self.view.save_button.config(command=self.save_button_clicked)
        self.view.tkraise()

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.show_error(error)

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        
        #self.save(self.view.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.view.message_label['text'] = message
        self.view.message_label['foreground'] = 'red'
        self.view.message_label.after(3000, self.hide_message)
        self.view.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.view.message_label['text'] = message
        self.view.message_label['foreground'] = 'green'
        self.view.message_label.after(3000, self.hide_message)

        # reset the form
        self.view.email_entry['foreground'] = 'black'
        self.view.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.view.message_label['text'] = ''