namespace CS102_Section3
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.plusbtn = new System.Windows.Forms.Button();
            this.minusbtn = new System.Windows.Forms.Button();
            this.multiplybtn = new System.Windows.Forms.Button();
            this.Dividebtn = new System.Windows.Forms.Button();
            this.txt2 = new System.Windows.Forms.TextBox();
            this.txt1 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // plusbtn
            // 
            this.plusbtn.Font = new System.Drawing.Font("Segoe UI", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.plusbtn.Location = new System.Drawing.Point(632, 47);
            this.plusbtn.Name = "plusbtn";
            this.plusbtn.Size = new System.Drawing.Size(75, 68);
            this.plusbtn.TabIndex = 0;
            this.plusbtn.Text = "+";
            this.plusbtn.UseVisualStyleBackColor = true;
            this.plusbtn.Click += new System.EventHandler(this.plusbtn_Click);
            // 
            // minusbtn
            // 
            this.minusbtn.Font = new System.Drawing.Font("Segoe UI", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.minusbtn.Location = new System.Drawing.Point(632, 121);
            this.minusbtn.Name = "minusbtn";
            this.minusbtn.Size = new System.Drawing.Size(75, 68);
            this.minusbtn.TabIndex = 1;
            this.minusbtn.Text = "-";
            this.minusbtn.UseVisualStyleBackColor = true;
            this.minusbtn.Click += new System.EventHandler(this.minusbtn_Click);
            // 
            // multiplybtn
            // 
            this.multiplybtn.Font = new System.Drawing.Font("Segoe UI", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.multiplybtn.Location = new System.Drawing.Point(632, 195);
            this.multiplybtn.Name = "multiplybtn";
            this.multiplybtn.Size = new System.Drawing.Size(75, 68);
            this.multiplybtn.TabIndex = 2;
            this.multiplybtn.Text = "x";
            this.multiplybtn.UseVisualStyleBackColor = true;
            this.multiplybtn.Click += new System.EventHandler(this.multiplybtn_Click);
            // 
            // Dividebtn
            // 
            this.Dividebtn.Font = new System.Drawing.Font("Segoe UI", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.Dividebtn.Location = new System.Drawing.Point(632, 269);
            this.Dividebtn.Name = "Dividebtn";
            this.Dividebtn.Size = new System.Drawing.Size(75, 68);
            this.Dividebtn.TabIndex = 3;
            this.Dividebtn.Text = "÷";
            this.Dividebtn.UseVisualStyleBackColor = true;
            this.Dividebtn.Click += new System.EventHandler(this.Dividebtn_Click);
            // 
            // txt2
            // 
            this.txt2.Location = new System.Drawing.Point(370, 216);
            this.txt2.Name = "txt2";
            this.txt2.Size = new System.Drawing.Size(163, 23);
            this.txt2.TabIndex = 4;
            // 
            // txt1
            // 
            this.txt1.Location = new System.Drawing.Point(370, 153);
            this.txt1.Name = "txt1";
            this.txt1.Size = new System.Drawing.Size(163, 23);
            this.txt1.TabIndex = 5;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.label1.Location = new System.Drawing.Point(238, 148);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(126, 28);
            this.label1.TabIndex = 6;
            this.label1.Text = "First Number";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.label2.Location = new System.Drawing.Point(210, 211);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(154, 28);
            this.label2.TabIndex = 7;
            this.label2.Text = "Second Number";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(378, 224);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(0, 15);
            this.label3.TabIndex = 8;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Segoe UI", 22F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.label4.Location = new System.Drawing.Point(303, 296);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(116, 41);
            this.label4.TabIndex = 9;
            this.label4.Text = "RESULT";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txt1);
            this.Controls.Add(this.txt2);
            this.Controls.Add(this.Dividebtn);
            this.Controls.Add(this.multiplybtn);
            this.Controls.Add(this.minusbtn);
            this.Controls.Add(this.plusbtn);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button plusbtn;
        private Button minusbtn;
        private Button multiplybtn;
        private Button Dividebtn;
        private TextBox txt2;
        private TextBox txt1;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
    }
}