using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ProjectRYPK
{
    public partial class OpenMain : Form
    {
        public OpenMain()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {


            List<string> password = SQLRequests.SelectRequest(
            "select Пароль from Агент where Логин = @pass",
           new string[] { "pass" }, new string[] { textBox1.Text });


            List<string> idtur = SQLRequests.SelectRequest(
               "select КодАгента from Агент where Логин = @pass",
               new string[] { "pass" }, new string[] { textBox1.Text });





            if (password.Count == 0)
            {
                MessageBox.Show("нет логина");
                return;
            }
            NomClass.id = idtur[0];

            if (password[0] != textBox2.Text)
            {
                MessageBox.Show("Пароль неправильный");
                return;
            }

            bool flag = false;

            if (textBox1.Text == "turagent1" & textBox2.Text == "123")
            {
                MF KLForm = new MF();
                this.Hide();
                KLForm.ShowDialog();
                this.Show();

                flag = true;
            }
            if (textBox1.Text == "sysadmin" & textBox2.Text == "123")
            {
                MF KLform = new MF();
                this.Hide();
                KLform.ShowDialog();
                this.Show();
                flag = true;

            }
            if (textBox1.Text == "sysadmin1" & textBox2.Text == "123456")
            {
                MF KLform = new MF();
                this.Hide();
                KLform.ShowDialog();
                this.Show();
                flag = true;
            }
            if (flag == false)
            {
                MessageBox.Show("No");
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {

            bool flag = false;
            if (textBox1.Text == "admin" & textBox2.Text == "123456")
            {
                MFAdmin opn = new MFAdmin();
                this.Hide();
                opn.ShowDialog();
                this.Show();
                flag = true;
            }

            if (textBox1.Text == " " && textBox2.Text == " ")
            {

                MessageBox.Show("Данные введены не до конца");
                return;
            }

            if (flag == false)
            {
                MessageBox.Show("Вход не выполнен");
            }


        }
    }
}
