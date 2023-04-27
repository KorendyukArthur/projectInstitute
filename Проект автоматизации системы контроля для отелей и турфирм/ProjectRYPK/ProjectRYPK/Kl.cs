﻿using System;
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
    public partial class Kl : Form
    {
        public Kl()
        {
            InitializeComponent();
        }

        private void Kl_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            List<string> idfamil = SQLRequests.SelectRequest(
             "select КодКлиента from ИКлиент where Фамилия = @pass",
             new string[] { "pass" }, new string[] { textBox2.Text });

            string kod = idfamil[0];



            List<string> insertion_Customers2 = SQLRequests.SelectRequest(
                "DELETE FROM Данные_клиента Where КодКлиента  = @d1", new string[] { "d1" }, new string[]
                { kod });

            List<string> insertion_Customers1 = SQLRequests.SelectRequest(
                "DELETE FROM ИКлиент Where Фамилия = @v1", new string[] { "v1" }, new string[]
                { textBox2.Text});
            //select Почта from Данные_клиента, ИКлиент 
            //  WHERE Данные_клиента.КодКлиента = ИКлиент.КодКлиента


            MessageBox.Show("Операция удаления прошла успешно");



        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            List<string> insertion_Customers = SQLRequests.SelectRequest(
"INSERT INTO ИКлиент (Фамилия, Имя, Отчество,Возраст) VALUES (@v1, @v2, @v3, @v4)", new string[] { "v1", "v2", "v3", "v4" }, new string[] { t1.Text, t2.Text, t3.Text, textBox1.Text });


            List<string> insertion_Customers1 = SQLRequests.SelectRequest(
            "INSERT INTO Данные_клиента (Адрес, ДанныеПаспорта, ДанныеЗагранпаспорта, НомерТелефона, Почта, ИННКлиента) VALUES (@a1, @a2, @a3, @a4, @a5, @a6)", new string[] { "a1", "a2", "a3", "a4", "a5", "a6" }, new string[] { a1.Text, a2.Text, a3.Text, a4.Text, a5.Text, a6.Text });

            MessageBox.Show("Регистрация прошла успешно");

        }

        private void button4_Click(object sender, EventArgs e)
        {
            List<string> idfamil = SQLRequests.SelectRequest(
         "SELECT Путевки.НаименованиеПутевки FROM  Путевки left join  Договор on Договор.КодПутевки = Путевки.КодПутевки left join ИКлиент on ИКлиент.КодКлиента = Договор.КодКлиента",
         new string[] { }, new string[] { });
            labels1.Text = "Наименование путевки" + "\n";
            for (int i = 0; i < idfamil.Count; i++)
            {
                labels1.Text += idfamil[i] + "\n";
            }


            List<string> idfamil1 = SQLRequests.SelectRequest(
           "SELECT ИКлиент.Фамилия FROM  Путевки left join  Договор on Договор.КодПутевки = Путевки.КодПутевки left join ИКлиент on ИКлиент.КодКлиента = Договор.КодКлиента",
           new string[] { }, new string[] { });
            labels2.Text = "Фамилия клиента" + "\n";
            for (int i = 0; i < idfamil1.Count; i++)
            {
                labels2.Text += idfamil1[i] + "\n";
            }

            List<string> idfamil2 = SQLRequests.SelectRequest(
           "SELECT Договор.КодДоговора FROM  Путевки left join  Договор on Договор.КодПутевки = Путевки.КодПутевки left join ИКлиент on ИКлиент.КодКлиента = Договор.КодКлиента",
           new string[] { }, new string[] { });
            labels3.Text = "Код договора" + "\n";
            for (int i = 0; i < idfamil2.Count; i++)
            {
                labels3.Text += idfamil2[i] + "\n";
            }


            List<string> idfamil3 = SQLRequests.SelectRequest(
          "SELECT Договор.Оплата FROM  Путевки left join  Договор on Договор.КодПутевки = Путевки.КодПутевки left join ИКлиент on ИКлиент.КодКлиента = Договор.КодКлиента",
          new string[] { }, new string[] { });
            labels4.Text = "Оплата путевки" + "\n";
            for (int i = 0; i < idfamil3.Count; i++)
            {
                labels4.Text += idfamil3[i] + "\n";
            }
        }
    }
}
