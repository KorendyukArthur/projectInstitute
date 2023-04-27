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
    public partial class Agent : Form
    {
        public Agent()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox2.Text == textBox3.Text)
            {

                List<string> insertion_Customers = SQLRequests.SelectRequest(
                "INSERT INTO Агент (Фамилия, Имя, Отчество, Логин, Пароль ) VALUES (@w1, @w2, @w3, @w4, @w5)", new string[] { "w1", "w2", "w3", "w4", "w5" }, new string[] { tr1.Text, tr2.Text, tr3.Text, textBox1.Text, textBox2.Text });

                List<string> insertion_Customers1 = SQLRequests.SelectRequest(
                "INSERT INTO ДанныеАгента (АдресАгента, ДанныеПаспорта, Должность, НомерТелефона, Почта, ИННАгента) VALUES (@a1, @a2, @a3, @a4, @a5, @a6)", new string[] { "a1", "a2", "a3", "a4", "a5", "a6" }, new string[] { ar1.Text, ar2.Text, ar3.Text, ar4.Text, ar5.Text, ar6.Text });

                MessageBox.Show("Регистрация прошла успешно");
            }
            else
            {

                MessageBox.Show("Пароль не повторяется");
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {

            List<string> idfamil1 = SQLRequests.SelectRequest(
           "SELECT Агент.Фамилия FROM  Агент ",
           new string[] { }, new string[] { });
            labels1.Text = "Фамилия Агент" + "\n";
            for (int i = 0; i < idfamil1.Count; i++)
            {
                labels1.Text += idfamil1[i] + "\n";
            }

            List<string> idfamil3 = SQLRequests.SelectRequest(
           "SELECT Агент.Имя FROM  Агент ",
           new string[] { }, new string[] { });
            labels2.Text = "Имя Агента" + "\n";
            for (int i = 0; i < idfamil3.Count; i++)
            {
                labels2.Text += idfamil3[i] + "\n";
            }


            List<string> idfamil2 = SQLRequests.SelectRequest(
           "SELECT ДанныеАгента.Должность FROM  ДанныеАгента left join  Агент on Агент.КодАгента = ДанныеАгента.КодАгента",
           new string[] { }, new string[] { });
            labels3.Text = "Должность" + "\n";
            for (int i = 0; i < idfamil2.Count; i++)
            {
                labels3.Text += idfamil2[i] + "\n";
            }

            List<string> idfamil4 = SQLRequests.SelectRequest(
           "SELECT ДанныеАгента.НомерТелефона FROM  ДанныеАгента left join  Агент on Агент.КодАгента = ДанныеАгента.КодАгента",
           new string[] { }, new string[] { });
            labels4.Text = "Номер телефона" + "\n";
            for (int i = 0; i < idfamil4.Count; i++)
            {
                labels4.Text += idfamil4[i] + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            List<string> idfamil = SQLRequests.SelectRequest(
            "select КодАгента from Агент where Фамилия = @pass",
            new string[] { "pass" }, new string[] { textBox4.Text });

            string kod = idfamil[0];



            List<string> insertion_Customers2 = SQLRequests.SelectRequest(
                "DELETE FROM ДанныеАгента Where КодАгента  = @d1", new string[] { "d1" }, new string[]
                { kod });

            List<string> insertion_Customers1 = SQLRequests.SelectRequest(
                "DELETE FROM Агент Where Фамилия = @v1", new string[] { "v1" }, new string[]
                { textBox4.Text});
            //select Почта from Данные_клиента, ИКлиент 
            //  WHERE Данные_клиента.КодКлиента = ИКлиент.КодКлиента
        }
    }
}
