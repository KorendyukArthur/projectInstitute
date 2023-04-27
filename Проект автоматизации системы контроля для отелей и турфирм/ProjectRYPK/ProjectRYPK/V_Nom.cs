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
    public partial class V_Nom : Form
    {
        public V_Nom()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text != "")
            {

                List<string> idfamil = SQLRequests.SelectRequest(
              "select КодПутевки from Путевки WHERE НаименованиеПутевки = @pass22",
              new string[] { "pass22" }, new string[] { comboBox1.Text });

                string a;


                try
                {
                    a = idfamil[0];
                }
                catch
                {
                    MessageBox.Show("Нет тура по данному id");
                    return;
                }



                label1.Text = "Наименование путевки" + "\n";
                List<string> idfamil1 = SQLRequests.SelectRequest(
                 "select НаименованиеПутевки from  Путевки WHERE Путевки.КодПутевки = @pass",
                 new string[] { "pass" }, new string[] { a });

                try
                {
                    label1.Text += idfamil1[0] + "\n";
                }
                catch
                {
                    MessageBox.Show("Нет агента по данному id");
                    return;
                }

                label2.Text = "Цена путевки" + "\n";
                List<string> idfamil2 = SQLRequests.SelectRequest(
                 "select ЦенаПутевки from  Путевки WHERE Путевки.КодПутевки  = @pass2",
                 new string[] { "pass2" }, new string[] { a });
                label2.Text += idfamil2[0] + "\n";

                label3.Text = "Дата начала" + "\n";
                List<string> idfamil3 = SQLRequests.SelectRequest(
                 "select ДатаНачала from  Путевки WHERE Путевки.КодПутевки  = @pass3",
                 new string[] { "pass3" }, new string[] { a });
                label3.Text += idfamil3[0] + "\n";



                label4.Text = "Дата окончания" + "\n";
                List<string> idfamil4 = SQLRequests.SelectRequest(
                 "select  ДатаОкончания from  Путевки WHERE Путевки.КодПутевки = @pass4",
                 new string[] { "pass4" }, new string[] { a });
                label4.Text += idfamil4[0] + "\n";

                label5.Text = "Страна путевки" + "\n";
                List<string> idfamil5 = SQLRequests.SelectRequest(
                 "select СтранаПутевки from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass5",
                 new string[] { "pass5" }, new string[] { a });
                label5.Text += idfamil5[0] + "\n";


                label6.Text = "Тип отеля" + "\n";
                List<string> idfamil6 = SQLRequests.SelectRequest(
                 "select  ТипОтеля from  ИнформацияПоПутевки  WHERE ИнформацияПоПутевки.КодПутевки = @pass6",
                 new string[] { "pass6" }, new string[] { a });
                label6.Text += idfamil6[0] + "\n";


                label7.Text = "Тип номера" + "\n";
                List<string> idfamil7 = SQLRequests.SelectRequest(
                 "select ТипНомера from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass7",
                 new string[] { "pass7" }, new string[] { a });
                label7.Text += idfamil7[0] + "\n";


                label8.Text = "Город" + "\n";
                List<string> idfamil8 = SQLRequests.SelectRequest(
                 "select Город from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass8",
                 new string[] { "pass8" }, new string[] { a });
                label8.Text += idfamil8[0] + "\n";


                label9.Text = "Улица" + "\n";
                List<string> idfamil9 = SQLRequests.SelectRequest(
                 "select Улица from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass9",
                 new string[] { "pass9" }, new string[] { a });
                label9.Text += idfamil9[0] + "\n";


                label10.Text = "Название отеля" + "\n";
                List<string> idfamil10 = SQLRequests.SelectRequest(
                 "select НазваниеОтеля from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass9",
                 new string[] { "pass9" }, new string[] { a });
                label10.Text += idfamil10[0] + "\n";
            }
            else
            {
                MessageBox.Show("Нет данных");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            label1.Text = " "; label2.Text = " "; label3.Text = " "; label4.Text = " ";
            label5.Text = " "; label6.Text = " "; label7.Text = " "; label8.Text = " ";
            label9.Text = " ";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            List<string> insertion_Customers2 = SQLRequests.SelectRequest(
               "DELETE FROM Договор Where КодДоговора  = @d1", new string[] { "d1" }, new string[]
               { textBox1.Text });
            MessageBox.Show("Удаление прошло успешно");

        }

        private void button4_Click(object sender, EventArgs e)
        {

            List<string> insertion_Customers2 = SQLRequests.SelectRequest(
                "DELETE FROM Путевки Where КодПутевки  = @d1", new string[] { "d1" }, new string[]
                { textBox1.Text});

            List<string> insertion_Customers1 = SQLRequests.SelectRequest(
                "DELETE FROM ИнформацияПоПутевки Where КодПутевки = @v1", new string[] { "v1" }, new string[]
                { textBox1.Text});

        }

        private void button2_Click(object sender, EventArgs e)
        {

            label1.Text = "Номер договора" + "\n";
            List<string> idfamil = SQLRequests.SelectRequest(
              "select КодДоговора from Договор ",
              new string[] { }, new string[] { });
            for (int i = 0; i < idfamil.Count; i++)
            {
                label1.Text += idfamil[i] + "\n";
            }

            label2.Text = "Дата оформления" + "\n";
            List<string> idfamil1 = SQLRequests.SelectRequest(
              "select ДатаОформления from Договор ",
              new string[] { }, new string[] { });
            for (int i = 0; i < idfamil1.Count; i++)
            {
                label2.Text += idfamil1[i] + "\n";
            }

            label3.Text = "Номер клиента" + "\n";
            List<string> idfamil2 = SQLRequests.SelectRequest(
              "select КодКлиента from Договор ",
              new string[] { }, new string[] { });

            for (int i = 0; i < idfamil2.Count; i++)
            {
                label3.Text += idfamil2[i] + "\n";
            }


            label4.Text = "Оплата путевки" + "\n";
            List<string> idfamil3 = SQLRequests.SelectRequest(
              "select Оплата from Договор ",
              new string[] { }, new string[] { });

            for (int i = 0; i < idfamil3.Count; i++)
            {
                label4.Text += idfamil3[i] + "\n";
            }

            label5.Text = "Номер Путевки" + "\n";
            List<string> idfamil4 = SQLRequests.SelectRequest(
             "select КодПутевки from Договор ",
             new string[] { }, new string[] { });

            for (int i = 0; i < idfamil4.Count; i++)
            {
                label5.Text += idfamil4[i] + "\n";
            }


            label6.Text = "Номер Агента" + "\n";
            List<string> idfamil5 = SQLRequests.SelectRequest(
             "select КодАгента from Договор ",
             new string[] { }, new string[] { });

            for (int i = 0; i < idfamil5.Count; i++)
            {
                label6.Text += idfamil5[i] + "\n";
            }

        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (comboBox3.Text != "")
            {
                List<string> idfamil = SQLRequests.SelectRequest(
                  "select КодКлиента from ИКлиент where ИКлиент.КодКлиента = @pass",
                  new string[] { "pass" }, new string[] { comboBox3.Text });
                string a;

                try
                {
                     a = idfamil[0];
                }
                catch
                {
                    MessageBox.Show("Нет агента по данному id");
                    return;
                }



                label1.Text = "Фамилия клиента" + "\n";
                List<string> idfamil1 = SQLRequests.SelectRequest(
                 "select Фамилия from  ИКлиент WHERE ИКлиент.КодКлиента  = @pass1",
                 new string[] { "pass1" }, new string[] { a });

                label1.Text += idfamil1[0] + "\n";



                label2.Text = "Имя клиента" + "\n";
                List<string> idfamil2 = SQLRequests.SelectRequest(
                 "select Имя from  ИКлиент WHERE ИКлиент.КодКлиента  = @pass2",
                 new string[] { "pass2" }, new string[] { a });

                label2.Text += idfamil2[0] + "\n";

                label3.Text = "Отчество" + "\n";
                List<string> idfamil3 = SQLRequests.SelectRequest(
                 "select Отчество from  ИКлиент WHERE ИКлиент.КодКлиента  = @pass3",
                 new string[] { "pass3" }, new string[] { a });

                label3.Text += idfamil3[0] + "\n";

                label17.Text = "Возраст" + "\n";
                List<string> idfamil17 = SQLRequests.SelectRequest(
                 "select Отчество from  ИКлиент WHERE ИКлиент.КодКлиента  = @pass13",
                 new string[] { "pass13" }, new string[] { a });

                label17.Text += idfamil17[0] + "\n";


                label4.Text = "ИНН клиента" + "\n";
                List<string> idfamil4 = SQLRequests.SelectRequest(
                 "select  ИННКлиента from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass4",
                 new string[] { "pass4" }, new string[] { a });

                label4.Text += idfamil4[0] + "\n";


                label5.Text = "Номер телефона" + "\n";
                List<string> idfamil5 = SQLRequests.SelectRequest(
                 "select  НомерТелефона from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass5",
                 new string[] { "pass5" }, new string[] { a });

                label5.Text += idfamil5[0] + "\n";


                label6.Text = "Адрес" + "\n";
                List<string> idfamil6 = SQLRequests.SelectRequest(
                 "select  Адрес from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass6",
                 new string[] { "pass6" }, new string[] { a });

                label6.Text += idfamil6[0] + "\n";


                label7.Text = "Данные паспорта" + "\n";
                List<string> idfamil7 = SQLRequests.SelectRequest(
                 "select ДанныеПаспорта from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass7",
                 new string[] { "pass7" }, new string[] { a });

                label7.Text += idfamil7[0] + "\n";


                label8.Text = "Данные загранпаспорта" + "\n";
                List<string> idfamil8 = SQLRequests.SelectRequest(
                 "select ДанныеЗагранпаспорта from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass8",
                 new string[] { "pass8" }, new string[] { a });

                label8.Text += idfamil8[0] + "\n";


                label9.Text = "Почта" + "\n";
                List<string> idfamil9 = SQLRequests.SelectRequest(
                 "select Почта from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass9",
                 new string[] { "pass9" }, new string[] { a });

                label9.Text += idfamil9[0] + "\n";
            }
            else
            {
                MessageBox.Show("Нет данных");
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {

            if (comboBox2.Text != "")
            {
                List<string> idfamild = SQLRequests.SelectRequest(
                  "select Фамилия from Агент where КодАгента = @pass",
                  new string[] { "pass" }, new string[] { comboBox2.Text });
                try
                    {
                    string b = idfamild[0];
                    }
                catch
                {
                    MessageBox.Show("Нет агента по данному id");
                    return;
                }


                label1.Text = "Фамилия клиента" + "\n";
                List<string> idfamild1 = SQLRequests.SelectRequest(
                 "select Имя from  Агент WHERE КодАгента  = @pass1",
                 new string[] { "pass1" }, new string[] { comboBox2.Text });

                try
                {
                    label1.Text += idfamild1[0] + "\n";
                }
                catch
                {
                    MessageBox.Show("Нет агента по данному id");
                    return;
                }


                label2.Text = "Имя клиента" + "\n";
                List<string> idfamild2 = SQLRequests.SelectRequest(
                 "select Отчество from  Агент WHERE КодАгента  = @pass2",
                 new string[] { "pass2" }, new string[] { comboBox2.Text });

                label2.Text += idfamild2[0] + "\n";

                label3.Text = "Отчество" + "\n";
                List<string> idfamild3 = SQLRequests.SelectRequest(
                 "select Отчество from  Агент WHERE КодАгента  = @pass3",
                 new string[] { "pass3" }, new string[] { comboBox2.Text });

                label3.Text += idfamild3[0] + "\n";



                label4.Text = "Адрес " + "\n";
                List<string> idfamild4 = SQLRequests.SelectRequest(
                 "select  АдресАгента from  ДанныеАгента WHERE КодАгента = @pass4",
                 new string[] { "pass4" }, new string[] { comboBox2.Text });

                label4.Text += idfamild4[0] + "\n";


                label5.Text = "Номер телефона" + "\n";
                List<string> idfamild5 = SQLRequests.SelectRequest(
                 "select  НомерТелефона from  ДанныеАгента WHERE  КодАгента = @pass5",
                 new string[] { "pass5" }, new string[] { comboBox2.Text });

                label5.Text += idfamild5[0] + "\n";


                label6.Text = "Адрес" + "\n";
                List<string> idfamild6 = SQLRequests.SelectRequest(
                 "select  Должность from  ДанныеАгента WHERE КодАгента  = @pass6",
                 new string[] { "pass6" }, new string[] { comboBox2.Text });

                label6.Text += idfamild6[0] + "\n";


                label7.Text = "Данные паспорта" + "\n";
                List<string> idfamild7 = SQLRequests.SelectRequest(
                 "select ДанныеПаспорта from  ДанныеАгента " +
                 "WHERE КодАгента = @pass7",
                 new string[] { "pass7" }, new string[] { comboBox2.Text });

                label7.Text += idfamild7[0] + "\n";


                label8.Text = "Данные загранпаспорта" + "\n";
                List<string> idfamild8 = SQLRequests.SelectRequest(
                 "select Почта from  ДанныеАгента " +
                 "WHERE КодАгента = @pass8",
                 new string[] { "pass8" }, new string[] { comboBox2.Text });

                label8.Text += idfamild8[0] + "\n";


                label9.Text = "Почта" + "\n";
                List<string> idfamild9 = SQLRequests.SelectRequest(
                 "select Почта from  Данные_клиента WHERE Данные_клиента.КодКлиента = @pass9",
                 new string[] { "pass9" }, new string[] { comboBox2.Text });

                label9.Text += idfamild9[0] + "\n";
            }
            else
            {
                MessageBox.Show("Нет данных");
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {




            if (comboBox4.Text != "")
            {

                label1.Text = "Наименование путевки" + "\n";
                List<string> idfamil1 = SQLRequests.SelectRequest(
                 "select НаименованиеПутевки from  Путевки WHERE Путевки.КодПутевки = @pass",
                 new string[] { "pass" }, new string[] { comboBox4.Text });

                try
                {
                    label1.Text += idfamil1[0] + "\n";
                }
                catch
                {
                    MessageBox.Show("Нет агента по данному id");
                    return;
                }


                


                label2.Text = "Цена путевки" + "\n";
                List<string> idfamil2 = SQLRequests.SelectRequest(
                 "select ЦенаПутевки from  Путевки WHERE Путевки.КодПутевки  = @pass2",
                 new string[] { "pass2" }, new string[] { comboBox4.Text });
                label2.Text += idfamil2[0] + "\n";

                label3.Text = "Дата начала" + "\n";
                List<string> idfamil3 = SQLRequests.SelectRequest(
                 "select ДатаНачала from  Путевки WHERE Путевки.КодПутевки  = @pass3",
                 new string[] { "pass3" }, new string[] { comboBox4.Text });
                label3.Text += idfamil3[0] + "\n";



                label4.Text = "Дата окончания" + "\n";
                List<string> idfamil4 = SQLRequests.SelectRequest(
                 "select  ДатаОкончания from  Путевки WHERE Путевки.КодПутевки = @pass4",
                 new string[] { "pass4" }, new string[] { comboBox4.Text });
                label4.Text += idfamil4[0] + "\n";

                label5.Text = "Страна путевки" + "\n";
                List<string> idfamil5 = SQLRequests.SelectRequest(
                 "select СтранаПутевки from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass5",
                 new string[] { "pass5" }, new string[] { comboBox4.Text });
                label5.Text += idfamil5[0] + "\n";


                label6.Text = "Тип отеля" + "\n";
                List<string> idfamil6 = SQLRequests.SelectRequest(
                 "select  ТипОтеля from  ИнформацияПоПутевки  WHERE ИнформацияПоПутевки.КодПутевки = @pass6",
                 new string[] { "pass6" }, new string[] { comboBox4.Text });
                label6.Text += idfamil6[0] + "\n";


                label7.Text = "Тип номера" + "\n";
                List<string> idfamil7 = SQLRequests.SelectRequest(
                 "select ТипНомера from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass7",
                 new string[] { "pass7" }, new string[] { comboBox4.Text });
                label7.Text += idfamil7[0] + "\n";


                label8.Text = "Город" + "\n";
                List<string> idfamil8 = SQLRequests.SelectRequest(
                 "select Город from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass8",
                 new string[] { "pass8" }, new string[] { comboBox4.Text });
                label8.Text += idfamil8[0] + "\n";


                label9.Text = "Улица" + "\n";
                List<string> idfamil9 = SQLRequests.SelectRequest(
                 "select Улица from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass9",
                 new string[] { "pass9" }, new string[] { comboBox4.Text });
                label9.Text += idfamil9[0] + "\n";


                label10.Text = "Название отеля" + "\n";
                List<string> idfamil10 = SQLRequests.SelectRequest(
                 "select НазваниеОтеля from  ИнформацияПоПутевки WHERE ИнформацияПоПутевки.КодПутевки = @pass9",
                 new string[] { "pass9" }, new string[] { comboBox4.Text });
                label10.Text += idfamil10[0] + "\n";
            }
            else
            {
                MessageBox.Show("нет данных");
            }
        }
    }
}
